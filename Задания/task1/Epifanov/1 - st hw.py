from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('C:\Desktop\exe\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.rftoday.ru/_vse_zagolovki2')
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
infos = soup.find_all(attrs={"class": "title"})
revs = soup.find_all(attrs={"class": "source"})
#print(infos[0].text) - если нужно вывести только n-ый заголовок
for info, rev in zip(infos, revs):
    print(f"{info.text} ; Источник: {rev.text}")#Вывод всех заголовков новостей и их источников со страницы 1