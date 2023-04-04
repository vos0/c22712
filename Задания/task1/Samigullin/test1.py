from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service('C:/Users/rusta/OneDrive/Рабочий стол/ИНФА/инфа 2 сем/driver/chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://lafoy.ru/modnye-muzhskie-strizhki-2023-3052/')
time.sleep (10)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
haircuts = soup.find_all('h2', class_='tm8 post__title')

for i in range(0, 30):
    print(haircuts[i].text)
