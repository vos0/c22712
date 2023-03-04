from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service('D:\Games\data\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.volkswagen.ru/polo/')
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
car_names = soup.find_all('div', class_='avn001-2_name')
prices = soup.find_all('div', class_='avn001-2_price-container')
for car_name, price in zip(car_names, prices):
    print(f"Название машины:{car_name.text} | Цена: {price.text} рублей")