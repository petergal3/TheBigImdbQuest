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

        #create instance of FilmDataManager
        film_data_manager = FilmDataManager(self.driver)
        assert film_data_manager.is_title_matches()

        #scrape data from imdb
        df = film_data_manager.Scraper()
        assert film_data_manager.is_data_correct(df)

        #adjust rating
        df = film_data_manager.Review_penalizer(df)
        assert film_data_manager.is_penalizer_correct(df)

        #adjust rating
        df = film_data_manager.Oscar_calculator(df)
        assert film_data_manager.is_oscar_calculator_correct(df)

        #write data and test
        df = df.sort_values(by='rating_new', ascending=False)
        df.to_csv("film_data.csv", encoding="utf-8", index=False, sep='\t')
        print(pd.read_csv("film_data.csv", sep='\t'))
        assert film_data_manager.is_data_correct(df)

        print("Test scrape finished")

    def tearDown(self):
        print("End")


if __name__ == '__main__':
   unittest.main(exit=False)
