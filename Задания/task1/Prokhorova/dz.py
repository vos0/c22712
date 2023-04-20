import psycopg2
import wget
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4')

cursor = connection.cursor()

create_table = """ create table dresses 
    (id serial primary key, name varchar(200), sale varchar(50), price varchar(50), info varchar(50), picture varchar(200))"""

cursor.execute(create_table)
connection.commit()

driver = Service('D:\data\chromedriver.exe')
browser = webdriver.Chrome(service=driver)
browser.get('https://www.ozon.ru/category/platya-zhenskie-7502/')
html_code = browser.page_source
soup = BeautifulSoup(html_code, 'lxml')

names = []
sale = soup.find_all('div', class_="eg1 g3e")

price = soup.find_all('span', class_="a2a-a2")
info = soup.find_all('span', class_="je4")
picture = soup.find_all('div', class_="k1m")

products = soup.find_all("div", class_="k7o o7k")
for product in products:
    names.append(soup.find('span', class_="m2e e3m m3e m5e tsBodyL k7l l7k").text.strip())

print(names)
exit(0)

for i in range(20):
    url = picture[i].find('img').attrs['src']
    file_name = f"C:\\Users\\Honor\\Desktop\\учеба\\прога\\pictures\\{i}.jpg"
    wget.download(url, file_name)
    ins_table = f"""insert into public.dresses(name, sale, price, info, picture) values ('{name[i].text}', '{sale[i].text}', '{price[i].text}', '{info[i].text}', '{file_name}')"""
    cursor.execute(ins_table)
    connection.commit()




cursor.close()

connection.close()