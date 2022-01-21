import unittest
from selenium import webdriver
from page import *

class Webscraper(unittest.TestCase):

    def setUp(self):
        print("Setup")
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get("https://www.imdb.com/chart/top")
        print("Setup finished")

    def test_search(self):
        filmhandler = FilmHandler(self.driver)
        filmhandler.is_title_matches()
        filmhandler.Scraper()
        print("test")

    def tearDown(self):
        print("End")


if __name__ == '__main__':
   unittest.main(exit=False)
