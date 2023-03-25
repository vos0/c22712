
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service("С:\DATA\ChromeDriver\chromedriver.exe")
browser = webdriver.Chrome(service=s)
browser.get("https://online.metro-cc.ru/category/sladosti-chipsy-sneki/shokolad-batonchiki?from=under_search&is_action=1")
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
products = soup.find_all('a', class_="product-card-name reset-link catalog-2-level-product-card__name style--catalog-2-level-product-card")
prices = soup.find_all('span', class_="product-card-prices__actual color-red")
for product,price in zip(products, prices):
    print(f"Продукт: {product.text[3:]}Цена: {price.text}")
    print("-"*100)