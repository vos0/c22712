from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("E:\data\chromedriver.exe")
browser = webdriver.Chrome(service=s)
browser.get("https://ria.ru/")
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
news = soup.find_all('div', class_='cell cell-list')
for new in news:
    print(new.text)
