from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('D:\Games\data\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.kinopoisk.ru/list/movies/top250/')
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
films=soup.find_all('div', class_='base-movie-main-info_mainInfo__Zl_u3')

for film in films:
    print(film.text)
