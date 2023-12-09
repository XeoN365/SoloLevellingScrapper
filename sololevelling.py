from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json


class Scrapper:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--ignore-certificate-errors")
        self.solo_levelling_website = "https://sololeveling-manwha.com/"
        self.folder_location = "./chapters/"
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(5)
        self.chapter_list = dict()

    def get_chapter_list(self):
        self.driver.get(self.solo_levelling_website)
        chapter_list = self.driver.find_elements(
            By.XPATH, "//li[@id='ceo_latest_comics_widget-3']/ul/li"
        )
        for element in chapter_list:
            chapter_number = element.text.split(" ")[3].split("\n")[0]
            chapter_link = element.find_element(By.TAG_NAME, "a").get_attribute("href")
            self.chapter_list[chapter_number] = dict()
            self.chapter_list[chapter_number]["url"] = chapter_link
        return self.chapter_list

    def get_chapter(self, chapter_number):
        self.driver.get(self.chapter_list[chapter_number]["url"])
        images = self.driver.find_elements(
            By.XPATH, "//div[@class='entry-content']/div[@class='separator']/a/img"
        )
        self.chapter_list[chapter_number]["images"] = dict()
        for index, image in enumerate(images):
            image_url = image.get_attribute("src")
            self.chapter_list[chapter_number]["images"][index] = image_url

    def save_to_json(self):
        with open("chapter_list.json", "w") as f:
            json.dump(self.chapter_list, f)


if __name__ == "__main__":
    scrap = Scrapper()
    chapter_list = scrap.get_chapter_list()
    for chapter_number in chapter_list:
        scrap.get_chapter(chapter_number)
    scrap.save_to_json()
