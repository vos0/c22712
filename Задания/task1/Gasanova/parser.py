#made by dialuna (or just Diana Gasanova) <3
import requests
from bs4 import BeautifulSoup as bs
URL = "https://www.kinopoisk.ru/lists/movies/top-250-2020/"
r = requests.get(URL, timeout=10)
soup = bs(r.text, "html.parser") 
films = soup.find_all(attrs={"class": "styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj"})
for film in films:
    print(film.text)
