from bs4 import BeautifulSoup
from user_agent import generate_user_agent
import requests
import os
import datetime

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

    def get_image_source(self, url):
        headers = {'user-agent': generate_user_agent()}
        request = requests.get(url, headers=headers)
        if request.status_code != 200:
            raise Exception("No connection to website")
        
        soup = BeautifulSoup(request.text, 'html.parser')
        tag = soup.find(id='screenshot-image')
        img_source = tag.get('src', None)
        
        if img_source is None:
            raise Exception("Image source doesn't exist")
        
        return img_source
        
    def retrieve_images(self):
        img_sources = []
        
        for url in self.urls:
            try:
                img_source = self.get_image_source(url)
            except Exception as e:
                print(e)
                continue
            img_sources.append(img_source)
            
        if not img_sources:
            return

        os.mkdir(self.dir_name)
        
        for ind, img in enumerate(img_sources):
            img_title = f'image_{ind}' if ind else 'image'
            request = requests.get(img)
            if request.status_code != 200:
                print(f"Can't download image: {img}")
                continue
                            
            with open(os.path.join(self.dir_name,f'{img_title}.png'), 'wb') as f:
                f.write(request.content)
            
   
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
                break
            
            if choice.strip() == '2':
                urls = get_urls_from_input()
                break
        
            if choice.strip() == '0':
                return

        SD = ScreenshotDownload(urls)
        SD.retrieve_images()
        
    main()