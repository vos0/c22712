from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
s = Service('E:\\Downloads\\chromedriver_win32.zip\\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://trial-sport.ru/gds.php?s=51516&c1=1070639&c2=1070640')
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
product_name=soup.find_all('a', class_='title')
description=soup.find_all('span', class_='description')
for product_name, description in zip(product_name, description):
    print(f"Продукт: {product_name.text} \nОписание: {description.text}")
print(" ")
