import unittest
from selenium import webdriver

class Webscraper(unittest.TestCase):

    def setUp(self):
        print("Setup")
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get("https://www.imdb.com/")
        print("Setup finished")

    def test_search(self):
        print("test")

    def tearDown(self):
            print("End")


if __name__ == '__main__':
   unittest.main(exit=False)







