import unittest
from selenium import webdriver
from page import *

class Webscraper(unittest.TestCase):

    def setUp(self):
        print("Setup")
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get("https://www.imdb.com/chart/top")
        print("Setup finished")

    def test_scrape(self):
        print("Test scrape")
        filmhandler = FilmDataManager(self.driver)
        assert filmhandler.is_title_matches()
        df = filmhandler.Scraper()
        assert filmhandler.is_data_correct(df)

        df = filmhandler.Review_penalizer(df)

        df = filmhandler.Oscar_calculator(df)

    def tearDown(self):
        print("End")


if __name__ == '__main__':
   unittest.main(exit=False)
