from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

S = Service('D:\teach\Prog\chromedriver.exe') #Открыли драйвер для хрома
browser = webdriver.Chrome(service=S) #Инициировали в отдельную переменную
browser.get('https://www.kinopoisk.ru/lists/movies/top250/')
html_text = browser.page_source
time.sleep(20)
soup = BeautifulSoup(html_text, 'lxml')
films = soup.find_all('div', class_='base-movie-main-info_mainInfo__ZL_u3')
'''
print(soup)
print(films)
'''
for film in films:
    print(film.text)
