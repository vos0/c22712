from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("E:\data\chromedriver.exe")
browser = webdriver.Chrome(service=s)
browser.get("https://www.litres.ru/fedor-dostoevskiy/prestuplenie-i-nakazanie/")
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
books = soup.find_all('div', class_='biblio_book_descr')
for book in books:
    print(book.text)
