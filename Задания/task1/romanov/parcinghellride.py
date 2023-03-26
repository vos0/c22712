from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('C:\Desktop\exe\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.hellride.ru/catalog/zapchasti-dlya-tryukovyh-samokatov/deki')
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
prices = soup.find_all(attrs={"class": "product-card__price"})
titles = soup.find_all(attrs={"class": "product-card__title"})

for price, title in zip(prices, titles):
    print(f" название {title.text} ; цена: {price.text}")