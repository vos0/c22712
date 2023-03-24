from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
s = Service("C:\Driver\chromedriver.exe")
browser = webdriver.Chrome(service=s)
browser.get("https://mephi.ru/")
sleep(10)
html_text = browser.page_source
soup = BeautifulSoup(html_text, "lxml")
serv = soup.find_all("div", class_="views-field views-field-title menu-item menu-item-10702")
print(serv[0].text)
