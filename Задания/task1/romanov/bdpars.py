import wget
import psycopg2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
connection = psycopg2.connect(host='localhost', dbname='postgres',
                              user='postgres', password='Q1w2e3r4')

cursor = connection.cursor()

cr_qwery = """ create table parser 
    (id serial primary key,
     name varchar(60),
      price varchar(15),
       picture varchar(100))"""

cursor.execute(cr_qwery)
connection.commit()

s = Service('C:\Desktop\exe\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.hellride.ru/catalog/zapchasti-dlya-tryukovyh-samokatov/deki')
html_code = browser.page_source
soup = BeautifulSoup(html_code, 'lxml')

name = soup.find_all(attrs={"class": "product-card__title"})
price = soup.find_all(attrs={"class": "product-card__price"})
picture = soup.find_all(attrs={"class": "product-slider__slide-img swiper-lazy swiper-lazy-loaded"})
#for prices, names in zip(price, name,):
 #print(f" название {names.text} ; цена: {prices.text} ")
for i in range(len(name)):
    url = picture[i].attrs['src']
    filename = f"C:\\Users\\Михаил\PycharmProjects\pythonProject8\\venv\Pictures\{i}.jpg"
    wget.download(url, filename)
    ins_qwery = f"""insert into public.Parser(name, price, picture) 
    values ('{name[i].text}', '{price[i].text}', '{filename}')"""
    cursor.execute(ins_qwery)
    connection.commit()




cursor.close()

connection.close()