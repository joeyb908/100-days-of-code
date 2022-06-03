import requests
from bs4 import BeautifulSoup

# URL for top 100 movies
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

# grab the webpage
response = requests.get(URL)
url_webpage = response.text

# parse the webpage for all the movie titles
soup = BeautifulSoup(url_webpage, "html.parser")
raw_movie_titles = soup.find_all(name="h3", class_='title')

# parse every movie and ONLY the movie title text into a new list
# movie_titles = []
# for movie in raw_movie_titles:
#     text = movie.getText()
#     movie_titles.append(text)

# same thing but with a list comprehension
movie_titles = [movie.getText() for movie in raw_movie_titles]

# reverse the list
movie_titles.reverse()
# using list slice
# movies = movie_titles[::-1]

# open the movies text, if it exists
try:
    with open("movies.txt", mode="r") as data:
        movies = data.readlines()

# if it doesn't, write the movie list
except FileNotFoundError:
    with open("movies.txt", mode="w", encoding="UTF-8") as data:
        for movie in movie_titles:
            data.write(f"{movie}\n")