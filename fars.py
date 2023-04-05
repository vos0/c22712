from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import psycopg2
s = Service("C:\Driver\chromedriver.exe")
browser = webdriver.Chrome(service=s)
browser.get("https://drivenew.ru/layfkhaki/besplatno/top-10-vinodelcheskikh-khozyaystv-krasnodarskogo-kraya/")
sleep(1)
html_text = browser.page_source
soup = BeautifulSoup(html_text, "lxml")
name = soup.find_all("h2")
contacts = soup.find_all("div", class_="article-info")

address = []
number = []
for element in contacts:
    a = element.find_all("p")[1]
    n = element.find_all("p")[2]
    address.append(a)
    number.append(n)

pic = soup.find("div", class_="white-bg white-bg-text box-15-new").find_all("img")
picture = []
url = "https://drivenew.ru"
for i in pic:
    p = url + i.attrs.get("src")
    picture.append(p)


connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4t5')
cursor = connection.cursor()
create = """create table Distilleries
    (id serial primary key , Name varchar(100), Place varchar(200), Contacts varchar(100), ImageLink varchar(80));"""
cursor.execute(create)
connection.commit()
for j in range(10):
    qwery = f"insert into public.distilleries(Name, Place, Contacts, ImageLink) values('{name[j].text.strip()}', '{address[j].text.strip()}', '{number[j].text.strip()}', '{picture[j]}')"
    cursor.execute(qwery)
    connection.commit()
cursor.execute('select * from Distilleries')
print(cursor.fetchall())
cursor.close()
connection.close()