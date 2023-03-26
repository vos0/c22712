from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = Service('D:\GOGdriver\chromedriver.exe')
browser = webdriver.Chrome(service=driver)
browser.get('https://www.kinopoisk.ru/lists/movies/popular-films/')
html_code = browser.page_source
soup = BeautifulSoup(html_code, 'lxml')
name = soup.find_all('div', class_="desktop-list-main-info_secondaryTitleSlot__mc0mI")

print(soup)
print(name)

for i in name:
    print(i.text)