import pandas as pd
import warnings

#basepage for driver setup
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

#FilmDataManager class manages film scraping and data manipulation
class FilmDataManager(BasePage):
    #Test:
    def is_title_matches(self):
        return "IMDb" in self.driver.title

    def is_data_correct(self, df):
        conditions = []
        is_correct = False
        n = len(df.index)

        # check if every type of data is correct (max number of oscars in the world: 11)
        for i in range(n):
            conditions.append(isinstance(df["title"].values[i], str))
            conditions.append(df["oscars_number"].values[i] < 12)
            conditions.append(0 <= df["rating"].values[i] <= 10)
            conditions.append(isinstance(df["review_number"].values[i], int))

        if False not in conditions:
            is_correct = True

        return is_correct

    #private method for scraping the data by using href
    def _FilmDatascrape(self, movie_href):
        self.driver.get(movie_href)

        title = self.driver.find_element_by_class_name('TitleHeader__TitleText-sc-1wu6n3d-0').text
        oscars = self.driver.find_element_by_class_name('Awards__Content-sc-152rtbv-2').text

        oscars_num = 0

        if oscars.find("Oscar") != -1:
           oscars_num = [int(s) for s in oscars.split() if s.isdigit()][0]

        rating = self.driver.find_element_by_class_name('AggregateRatingButton__RatingScore-sc-1ll29m0-1').text
        details_button = self.driver.find_element_by_class_name('RatingBarButtonBase__Button-sc-15v8ssr-2')
        details_button.click()

        reviewer_num = self.driver.find_element_by_class_name('allText').find_element_by_class_name('ratingTable').find_element_by_class_name('smallcell').text
        reviewer_num = reviewer_num.replace(" ", "")

        to_append = [str(title), int(oscars_num), float(rating), int(reviewer_num)]
        return to_append

    def Data_maninpulator(self):
        return 0

    #returns the scraped data from films in pandas dataframe
    def Scraper(self):
        print('Scraping...')
        #not permanent
        warnings.filterwarnings("ignore")

        list_ = self.driver.find_element_by_class_name('lister-list').find_elements_by_tag_name('tr')
        df = pd.DataFrame(columns=["title", "oscars_number", "rating", "review_number"])
        number_of_films = 3
        titles = []
        imdb_links = []

        #collecting hrefs
        for i  in range(number_of_films):
            movie_href =  list_[i].find_element_by_class_name('titleColumn').find_element_by_tag_name('a').get_attribute('href')
            movie_title = list_[i].find_element_by_class_name('titleColumn').find_element_by_tag_name('a').text
            imdb_links.append(movie_href)
            titles.append(movie_title)

        #adding scraped data to df
        for i in range(number_of_films):
            film_info = self._FilmDatascrape(imdb_links[i])
            a_series = pd.Series(film_info, index=df.columns)
            df = df.append(a_series, ignore_index=True)

        print(df)
        print('Data scraped!')

        return df

    def Review_penalizer(self, df):
        max = df["review_number"].max()
        n = len(df.index)
        df["rating_new"] = df["rating"] - (((max - df["review_number"]) // 100000) / 10)
        print(df)

    def Oscar_calculator(self, df):
        return 0