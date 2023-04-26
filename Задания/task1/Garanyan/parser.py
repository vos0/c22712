from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import psycopg2
import wget

browser = webdriver.Chrome(service=Service('E:\data\chromedriver.exe'))
browser.get('https://8956food.ru/')
soup = BeautifulSoup(browser.page_source, "lxml")

Name = soup.find_all(attrs={"class": "subtitle"})
Price = soup.find_all(attrs={"class": "price"})
Image = soup.find_all(attrs={"class": "holder-img"})

connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4')
cursor = connection.cursor()
create_q = '''CREATE TABLE Food  
     (ID serial primary key, Name varchar(500), Price varchar(60), src varchar(100))'''
cursor.execute(create_q)
connection.commit()

#https://smartomato.ams3.cdn.digitaloceanspaces.com/uploads/media/photo/769221/dish_large__1.jpg
for j in range(15):
    url = Image[j].find('img').attrs['src']
    tempf = f"C:\\Users\\Harutyun\\Desktop\\prog\\food{j}.jpg"
    wget.download(url, tempf)
    insert_query = f'''INSERT into public.Food(Name, Price, src) values ('{Name[j].text}', '{Price[j].text}', '{tempf}') '''
    cursor.execute(insert_query)
connection.commit()

cursor.execute("SELECT * from Food")
print(cursor.fetchall())

cursor.close()
connection.close()