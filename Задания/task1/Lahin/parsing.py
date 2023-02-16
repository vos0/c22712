from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
s = Service("С:\DATA\ChromeDriver\chromedriver.exe")
browser = webdriver.Chrome(service=s)
browser.get("https://www.kinopoisk.ru/lists/movies/top250/")
sleep(15)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
films = soup.find_all('div', class_="desktop-list-main-info_secondaryTitleSlot__mc0mI")
for film in films:
    print(film.text)
    print("--------")
