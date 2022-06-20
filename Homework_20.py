import os
import requests


class DownloadJPG:

    def __init__(self, url, name):
        self.url = url
        self.response = None
        self.name = name

    def image_downloader(self):
        try:
            self.response = requests.get(self.url)
        except Exception as error:
            print("! SOMETHING WRONG !")
        if self.response.status_code == 200:
            print(f"SUCCESS: You can find your file '{self.name}' in path '{os.getcwd()}'")
            with open(f"{self.name}.jpg", "wb") as my_pic:
                my_pic.write(self.response.content)


my_file = DownloadJPG(url=input("Write URL for downloading...\n"), name=input("Write an image name\n"))
my_file.image_downloader()
# sample URL for checking : https://logicoretech.com/wp-content/uploads/2022/05/django-development-1-1024x683.jpg