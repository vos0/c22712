import psycopg2
import wget
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service("С:\DATA\ChromeDriver\chromedriver.exe")
browser = webdriver.Chrome(service=s)
browser.get("https://online.metro-cc.ru/virtual/assortiment_rioba-4887?from=under_search&page=2")
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
productst = soup.find_all('span', class_="product-card-name__text")
pricest = soup.find_all('span', class_="product-price__sum-rubles")
pictures = soup.find_all('img', class_="product-card-photo__image")
connection=psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4')
cursor = connection.cursor()
products, prices = [], []
for i in range(len(productst)):
    products.append(productst[i].text.replace("\n", "").strip())
    prices.append(pricest[i].text+" Р/шт")
insert = """CREATE TABLE public.Chocolate(
id serial primary key,
product varchar(100),
price varchar(25),
src varchar(50)
);
"""
cursor.execute(insert)
connection.commit()
for i in range(len(products)):
    url = pictures[i]['src']
    filename = f"C:\DATA\Images2\{i+1}.jpg"
    wget.download(url, filename)
    insert = f"""INSERT INTO public.Chocolate(
        product, price, src)
        VALUES
        ('{products[i]}', '{prices[i]}', '{filename}');"""
    cursor.execute(insert)
    connection.commit()
cursor.execute("select * from Chocolate")
print("Результат", cursor.fetchall())
cursor.close()
connection.close()
