from screendown import ScreenshotDownload, SSDownloadException
from PyQt5 import QtWidgets
from gui import *
import os, sys
import time
import requests


class App(QtWidgets.QWidget):
    def __init__(self):
        self.dir = os.getcwd()
        self.app = QtWidgets.QApplication(sys.argv)
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.Window)
        self.ui.dir_line.setText(self.dir)
        self.ui.load_button.clicked.connect(self.load_file)
        self.ui.dir_button.clicked.connect(self.select_dir)
        self.ui.submit_button.clicked.connect(self.download)
        self.ui.load_line.returnPressed.connect(self.open_file)
        self.ui.load_line.returnPressed.connect(self.set_dir)
        super().__init__()

    def log(self, message):
        local_time = time.localtime()
        now = time.strftime("%H:%M:%S", local_time)
        self.ui.logs_text.append(f"[{now}] {message}")

    def open_file(self):
        filename = self.ui.load_line.text()
        try:
            with open(filename, "r") as f:
                self.ui.links_text.setPlainText(f.read())
            self.log("File opened successfully")
        except:
            self.log("Couldn't open a file")

    def load_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open File", os.getcwd(), "Text files (*.txt);;All files (*)"
        )
        if filename:
            self.ui.load_line.setText(filename)
            self.open_file()

    def set_dir(self):
        self.dir = self.ui.dir_line.text()

    def select_dir(self):
        selected_directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if selected_directory:
            self.ui.dir_line.setText(selected_directory)
            self.set_dir()

    def download(self):
        urls = self.ui.links_text.toPlainText()
        obj = ScreenshotDownloadApp(urls, self.dir, self.ui.logs_text)
        obj.run()

    def run(self):
        self.Window.show()
        sys.exit(self.app.exec_())


class ScreenshotDownloadApp(ScreenshotDownload):
    def __init__(self, urls: list | tuple | str, dir, text_box) -> None:
        super().__init__(urls)
        self.text_box = text_box

    def log(self, message):
        local_time = time.localtime()
        now = time.strftime("%H:%M:%S", local_time)
        self.text_box.append(f"[{now}] {message}")

    def fetch_image_sources(self):
        img_sources = super().fetch_image_sources()
        for url in set(map(lambda x: self.extend_protocol(x), self.urls)).difference(
            set(map(lambda x: x[1], img_sources))
        ):
            self.log(f"Failed to parse {url}")
        return img_sources
        
    def save_image(self, img_title: str, content: bytes, url: str):
        try:
            with open(os.path.join(self.dir_name, f"{img_title}.png"), "wb") as f:
                f.write(content)
            self.log(f"File {url} saved as {img_title}")
        except Exception as e:
            self.log(f"Error while saving to file: {url}")
                
    def download_and_save(self, img_sources: list[tuple]):
        for ind, (img, url) in enumerate(img_sources):
            img_title = f"image_{ind}" if ind else "image"
            try:
                request = requests.get(img)
                if request.status_code != 200:
                    raise SSDownloadException
            except:
                self.log(f"Can't download image: {url}")
                continue

            self.save_image(img_title, request.content, url)

    def run(self):
        super().run()
        self.log("Screenshots downloaded")
