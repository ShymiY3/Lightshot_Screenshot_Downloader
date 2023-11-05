from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests
import os
import datetime


class SSDownloadException(Exception):
    pass


class ScreenshotDownload:
    """
    A class used to download screenshots from Lightshot website.

    ...

    Attributes
    ----------
    urls : list | tuple | str
        a list, tuple or string containing urls to download screenshots from
    dir_name : str
        a string containing the name of the directory where the screenshots will be saved

    Methods
    -------
    get_dir_name():
        Returns the name of the directory where the screenshots will be saved
    is_valid_url(url: str):
        Returns True if the url is valid, False otherwise
    is_valid_domain(url: str):
        Returns True if the url domain is valid, False otherwise
    make_request(url: str):
        Sends a GET request to the given url and returns the response
    scrape_image(request_text: str):
        Scrapes the image source from the given request text and returns it
    fetch_image_sources():
        Fetches the image sources from the given urls and returns them
    save_image(img_title: str, content: bytes):
        Saves the given image content to a file with the given title
    download_and_save(img_sources: list):
        Downloads and saves the images from the given sources
    run():
        Runs the screenshot download process
    """

    def __init__(self, urls: list | tuple | str, dir = None) -> None:
        """
        Constructs all the necessary attributes for the ScreenshotDownload object.

        Parameters
        ----------
            urls : list | tuple | str
                a list, tuple or string containing urls to download screenshots from
        """
        self.urls = self.format_url(urls)
        self.dir_name = self.get_dir_name(dir)

    def extend_protocol(self, url):
        url = url.strip()
        url = "https://" + url if not url.startswith("http") else url
        return url
    
    def format_url(self, urls):
        if isinstance(urls, str):
            urls = urls.split()

        return list(map(self.extend_protocol, urls))

    def get_dir_name(self, dir=None):
        """
        Returns the name of the directory where the screenshots will be saved.
        The directory name is based on the current date and a suffix number if necessary.

        Returns
        -------
        str
            the name of the directory where the screenshots will be saved
        """
        dir = os.getcwd() if dir is None else dir
        
        if not os.path.isdir(dir):
            raise Exception("Not valid directory")
        
        dirs = os.listdir(dir)
        today_str = str(datetime.date.today())
        suffix = 0

        for directory in dirs:
            if directory == today_str:
                suffix = 1
                continue

            if not directory.startswith(today_str):
                continue
            dir_suffix = directory.rsplit("_", 1)[-1]

            if not dir_suffix.isnumeric():
                continue
            suffix = max(suffix, int(dir_suffix) + 1)

        if suffix == 0:
            return today_str
        return os.path.join(dir, f"{today_str}_{suffix}")

    def is_valid_url(self, url: str):
        """
        Returns True if the url is valid, False otherwise.

        Parameters
        ----------
        url : str
            the url to check

        Returns
        -------
        bool
            True if the url is valid, False otherwise
        """
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False

    def is_valid_domain(self, url: str):
        """
        Returns True if the url domain is valid, False otherwise.

        Parameters
        ----------
        url : str
            the url to check

        Returns
        -------
        bool
            True if the url domain is valid, False otherwise
        """
        DOMAIN = "prnt.sc"
        try:
            return DOMAIN in urlparse(url).netloc
        except:
            return False

    def make_request(self, url: str):
        """
        Sends a GET request to the given url and returns the response.

        Parameters
        ----------
        url : str
            the url to send the request to

        Returns
        -------
        requests.Response
            the response from the server
        """
        user_agent = "'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'"
        headers = {"user-agent": user_agent}
        try:
            request = requests.get(url, headers=headers)
        except Exception as e:
            raise SSDownloadException(e)
        if request.status_code != 200:
            raise SSDownloadException("No connection to website")
        return request

    def scrape_image(self, request_text: str):
        """
        Scrapes the image source from the given request text and returns it.

        Parameters
        ----------
        request_text : str
            the text of the response from the server

        Returns
        -------
        str
            the image source url
        """
        soup = BeautifulSoup(request_text, "html.parser")
        tag = soup.find(id="screenshot-image")
        img_source = tag.get("src", None)

        if img_source is None:
            raise SSDownloadException("Image source doesn't exist")

        return img_source

    def fetch_image_sources(self):
        """
        Fetches the image sources from the given urls and returns them.

        Returns
        -------
        list
            a list of image source urls
        """
        img_sources = []
        for url in self.urls:
            if not (self.is_valid_url(url) and self.is_valid_domain(url)):
                print(f"Not valid input: {url}")
                continue
            try:
                request = self.make_request(url)
                img_source = self.scrape_image(request.text)
                print(f"Image link parsed from: {url}")
            except SSDownloadException as e:
                print(f"Error with url: {url}; {e}")
                continue
            img_sources.append((img_source, url))

        return img_sources

    def save_image(self, img_title: str, content: bytes, url: str):
        """
        Saves the given image content to a file with the given title.

        Parameters
        ----------
        img_title : str
            the title of the image file
        content : bytes
            the content of the image file
        """
        try:
            with open(os.path.join(self.dir_name, f"{img_title}.png"), "wb") as f:
                f.write(content)
            print(f"File {url} saved as {img_title}")
        except Exception as e:
            print(f"Error while saving to file: {url}")

    def download_and_save(self, img_sources: list[tuple]):
        """
        Downloads and saves the images from the given sources.

        Parameters
        ----------
        img_sources : list
            a list of image source urls
        """
        for ind, (img, url) in enumerate(img_sources):
            img_title = f"image_{ind}" if ind else "image"
            try:
                request = requests.get(img)
                if request.status_code != 200:
                    raise SSDownloadException
            except:
                print(f"Can't download image: {url}")
                continue

            self.save_image(img_title, request.content, url)

    def run(self):
        """
        Runs the screenshot download process.
        """
        img_sources = self.fetch_image_sources()

        if not img_sources:
            return
        os.mkdir(self.dir_name)
        self.download_and_save(img_sources)


if __name__ == "__main__":
    def get_urls_from_file():
        print("Urls in file must be separated by new line or space")
        file_path = str(input("Your file path: "))
        urls = []

        with open(file_path) as f:
            urls = f.read().split()

        return urls

    def get_urls_from_input():
        print(
            """
        Type in each url separated by new line or space. To end typing type "0".
        """
        )
        urls = []
        while True:
            url = str(input("Your url: "))
            if url == "0":
                break

            urls.extend(url.split())
        return urls

    def main():
        print(
            """Choose option:
    1. From file 
    2. From manual input
    0. Exit"""
        )
        while True:
            choice = str(input("Your choice: "))

            if choice.strip() == "1":
                urls = get_urls_from_file()
                print("URLS:")
                print(*urls, sep="\n")
                break

            if choice.strip() == "2":
                urls = get_urls_from_input()
                break

            if choice.strip() == "0":
                return

        SD = ScreenshotDownload(urls)
        SD.run()

    main()
