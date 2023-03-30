from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('D:\data\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.kfc.ru/')
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')

prices = soup.find_all(attrs={"class": "GFmMCzZoYv"})
titles = soup.find_all(attrs={"class": "_14ZQf5wtqx c-description"})

for price, title in zip(prices, titles):
    print(f" название {title.text} ; цена: {price.text}")