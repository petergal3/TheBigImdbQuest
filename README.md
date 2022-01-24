# TheBigImdbQuest

Project description:
  This application scrapes data of the top 20 films (Rating, Number of ratings, Number of Oscars, Title of the movie) from imdb's top 250 list (https://www.imdb.com/chart/top/).

  Then it adjusts the given rating by checking the given oscars and the number of reviews.
  The rule is:
    - Every 100k deviation from the maximum translates to a point deduction of 0.1. 
    - 1 or 2 oscars → 0.3 point, 3 or 5 oscars → 0.5 point, 6 - 10 oscars → 1 point, 10+ oscars → 1.5 point

  I used python in my project because I think it is the most popular and best known programming language. 
  Used packages: selenium for web automation, pandas for data structuring and unittest for testing.

  I made a class FilmDataManager that handles all methods that deals with film data, because I think it is always better to be able to make an instance of it.
  This way I can use more of them with different parameters.
  
  A FilmDataManager object has methods like Scrape() (scrape top 20 movie data from imdb), Oscar_calculator() (adjust rating by oscars number: details in the above written rule)
  and Review_penalizer() (adjust rating by review number: details in the above written rule).


Installation and Run Project:
  The project has a chromedriver.exe file in it. This chromedriver works with chrome version 97 and on windows only. If you would like to use it 
  with different versions of chrome you should download your chromedriver.exe from here: https://chromedriver.chromium.org/downloads
  After you have dawnloaded your file please put it in the project library and replace the old one.

Tests:

  I have written a test for every function:
  
    -  is_title_matches(self): checks if imdb is loaded
    -  is_data_correct(self, df): checks every column and every row if data type is correct
    -  is_penalizer_correct(self,df): checks if added row by Review_penalizer() is between the 0 and the biggest possible number
    -  is_oscar_calculator_correct(self,df): checks if added row by Oscar_calculator() is between 0 and 1.5
       
