import psycopg2
import wget
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4')

cursor = connection.cursor()

creat_qwery = """ create table Parser 
    (id serial primary key, product_name varchar(100), description varchar(1000), price varchar(10), priceDis varchar(30), scr varchar(100))"""

cursor.execute(creat_qwery)
connection.commit()

driver = Service('E:\\Downloads\\chromedriver_win32.zip\\chromedriver.exe')
browser = webdriver.Chrome(service=driver)
browser.get('https://trial-sport.ru/gds.php?s=51516&c1=1070639&c2=1070640')
html_code = browser.page_source
soup = BeautifulSoup(html_code, 'lxml')
product_name=soup.find_all('a', class_='title')
description=soup.find_all('span', class_='description')
price = soup.find_all('span', class_="price")
priceDis = soup.find_all('span', class_="discount")
pictures = soup.find_all('div', class_="img")

for i in range(15):
    url = 'https://trial-sport.ru/gds.php?s=51516&c1=1070639&c2=1070640'+pictures[i].find('a').find('img')['src']
    filename = f"E:\Downloads\parcing\img\{i}.jpg"
    wget.download(url, filename)
    ins_qwery = f"""insert into public.Parser(product_name, description, price, priceDis, scr)
        VALUES ('{product_name[i].text}','{description[i].text}', '{price[i].text}', '{priceDis[i].text}', '{filename}')"""
    connection.commit()




cursor.close()

connection.close()