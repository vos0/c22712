from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Selenium - библиотека для автоматизации действий веб браузера, скрапинга
# запускаем браузер
s = Service('C:\data\chrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.wildberries.ru/catalog/muzhchinam/odezhda/futbolki-i-mayki?bid=3b73ce5a-8eba-45a1-b9b2-0723f7592eac#c145658286')
time.sleep (10)#задержка для ввода капчи
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
films=soup.find_all('div', class_='/games/the-elder-scrolls-v-skyrim/')
ratings = soup.find_all('div', class_='KnbCardMark_label__hg6Pg tv-series-mark KnbCardMark_isGreen__G_FLl')
for film, rating in zip(films, ratings):
    print(f"Игра:{film.text} | Рейтинг:{rating.text}")


# Это пример парсинга. Вам необходимо спарсить 1 страницу каталога любого сайта на выбор.
#сайты не должны повторяться
# Спарсить необходимо только Заголовки и описание.