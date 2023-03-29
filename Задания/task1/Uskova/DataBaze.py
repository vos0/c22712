from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import psycopg2
import wget

connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4')
cursor = connection.cursor()

crtable = """ create table Notebooks
    (id serial primary key, name varchar(500), description varchar(500), code varchar(200), price varchar(100),
    picture varchar(500)) """

cursor.execute(crtable)
connection.commit()

s = Service('C:\\Users\\Yekaterina\\Downloads\\chromedriver_win32\\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.citilink.ru/catalog/noutbuki/')
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')

name = soup.find_all('div', class_='app-catalog-1tp0ino e1an64qs0')
description = soup.find_all('div', class_='app-catalog-1o4umte eevw8x70')
code = soup.find_all('div', class_= 'app-catalog-0 e1dsj6g20')
price = soup.find_all('div', class_= 'app-catalog-0 e1dsj6g20')
picture = soup.find_all('div', class_='app-catalog-0 e1jarwcz0')

for i in range(10):
    url = picture[i].find('img').attrs['src']
    file = f"C:\\Users\\Yekaterina\\Desktop\\baza\\pic{i}.JPG"
    wget.download(url, file)
    ins_qwery = f"""insert into public.Notebooks(name, description, code, price, picture)
    values ('{name[i].text}', '{description[i].text}', '{code[i].text}', '{price[i].text}','{file}')"""
    cursor.execute(ins_qwery)
    connection.commit()

cursor.close()
connection.close()
