from bs4 import BeautifulSoup
from user_agent import generate_user_agent
from urllib.parse import urlparse
import requests
import os
import datetime

class SSDownloadException(Exception):
    pass


class ScreenshotDownload:
    def __init__(self, urls) -> None:
        self.urls = urls
        if isinstance(urls, str):
            self.urls = [urls]
        self.dir_name = self.get_dir_name() 

    def get_dir_name(self):
        dirs = os.listdir()
        today_str = str(datetime.date.today())
        suffix = 0
        
        for directory in dirs:
            if directory == today_str:
                suffix = 1
                continue
            
            if not directory.startswith(today_str):
                continue
            dir_suffix = directory.rsplit('_', 1)[-1]
            
            if not dir_suffix.isnumeric():
                continue
            suffix = max(suffix, int(dir_suffix)+1)

        if suffix == 0:
            return today_str
        return f'{today_str}_{suffix}'
    
    def is_valid_url(self, url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False
        
    def is_valid_domain(self, url):
        DOMAIN = "prnt.sc"
        try:
            return DOMAIN in urlparse(url).netloc
        except:
            return False
        
    def make_request(self, url):
        headers = {'user-agent': generate_user_agent()}
        try:
            request = requests.get(url, headers=headers)
        except Exception as e:
            raise SSDownloadException(e)
        if request.status_code != 200:
            raise SSDownloadException("No connection to website")
        return request
        
    def scrape_image(self, request_text):
        soup = BeautifulSoup(request_text, 'html.parser')
        tag = soup.find(id='screenshot-image')
        img_source = tag.get('src', None)
        
        if img_source is None:
            raise SSDownloadException("Image source doesn't exist")
        
        return img_source
    
    def fetch_image_sources(self):
        img_sources = []
        for url in self.urls:
            url = url.strip()
            url = "https://" + url if not url.startswith("http") else url
            if not (self.is_valid_url(url) and self.is_valid_domain(url)): 
                continue
            try:
                request = self.make_request(url)
                img_source = self.scrape_image(request.text)
            except SSDownloadException as e:
                print(e)
                continue
            img_sources.append(img_source)    

        return img_sources
    
    def save_image(self, img_title, content):
        with open(os.path.join(self.dir_name,f'{img_title}.png'), 'wb') as f:
                f.write(content)
    
    def download_and_save(self, img_sources):
         for ind, img in enumerate(img_sources):
            img_title = f'image_{ind}' if ind else 'image'
            request = requests.get(img)
            if request.status_code != 200:
                print(f"Can't download image: {img}")
                continue
            self.save_image(img_title, request.content)
    
    def run(self):
        img_sources = self.fetch_image_sources()
        if not img_sources:
            return 
        os.mkdir(self.dir_name)
        self.download_and_save(img_sources)
    
   
if __name__ == '__main__':
    def get_urls_from_file():
        print("Urls in file must be separated by new line or space")
        file_path = str(input('Your file path: '))
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
            if url == '0':
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
            
            if choice.strip() == '1':
                urls = get_urls_from_file()
                print(*urls, sep='\n')
                break
            
            if choice.strip() == '2':
                urls = get_urls_from_input()
                break
        
            if choice.strip() == '0':
                return

        SD = ScreenshotDownload(urls)
        SD.run()
        
    main()