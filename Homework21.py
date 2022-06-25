import json
import os
import requests
import threading
import time
import datetime


class Image:
    def __init__(self, name, url, path=None):
        self.name = name
        self.url = self.validate_url(url)
        self.default_path = path if path else os.getcwd()

    def validate_url(self, url):
        response = self.send_request_safe(url)

        if response.status_code == 200:
            return url
        else:
            raise ValueError("Wrong url")

    @staticmethod
    def send_request_safe(url):
        while True:
            try:
                return requests.get(url)
            except requests.exceptions.ConnectionError:
                time.sleep(2)
                continue
            except Exception as err:
                raise Exception("something wrong has happened {}".format(err))

    def download(self):
        response = self.send_request_safe(self.url)

        if response.status_code == 200:
            img_address = f"{self.default_path}/{self.name}"
            with open(img_address, "wb") as file:
                file.write(response.content)

        print(f"Downloading,{self}")


class FromJson2Image:
    def __init__(self, json_file_path):
        self.json_file_path = self.validate_path(json_file_path)
        self.image_dict = self.read_from_json()
        self.image_list = self.create_images_from_dict()

    @staticmethod
    def validate_path(path):
        if not os.path.exists(path):
            raise ValueError("wrong path")

        return path

    def read_from_json(self):
        with open(self.json_file_path) as json_file:
            data = json.load(json_file)

        return data

    def create_images_from_dict(self):
        image_list = []
        for dict_ in self.image_dict:
            image_list.append(Image(name=dict_["img_name"], url=dict_["img_url"]))

        return image_list

    def download_all_images(self):
        for image in self.image_list:
            image.download()
            time.sleep(0.01)

    def download_all_images_by_threads(self):
        starting_time = datetime.datetime.today()
        print(f"{starting_time}, download_all_images")
        thread_list = []
        for image in self.image_list:
            x = threading.Thread(target=self.download_all_images(), args=(image,), daemon=True)
            thread_list.append(x)
            x.start()
            time.sleep(0.1)
        for thread in thread_list:
            thread.join()
        b = (datetime.datetime.today() - starting_time).seconds
        print(f"download_all_images took {b} seconds")


if __name__ == "__main__":
    json_to_image = FromJson2Image(json_file_path="image_links.json")
    #
    # json_to_image.download_all_images()
    json_to_image.download_all_images_by_threads()
