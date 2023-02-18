from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('C:\Desktop\exe\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://pythonpip.ru/examples/kak-posmotret-ustanovlennye-moduli-python-i-vyvesti-ih-spisok')
html_text = browser.page_source
print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
infos = soup.find_all(attrs={"class":"relpost-block-single-text"})
for info in infos:
    print(info.text)
