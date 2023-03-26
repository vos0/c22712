from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import psycopg2
import wget

browser = webdriver.Chrome(service=Service('C:\Desktop\exe\chromedriver.exe'))
browser.get('https://flawery.ru/moscow/bouquets/color-blue/?min=0&max=max&sorting=discount')
soup = BeautifulSoup(browser.page_source, "lxml")
Name = soup.find_all(attrs={"class": "catalog_title"})
Price = soup.find_all(attrs={"class": "catalog_price_now"})
Discount = soup.find_all(attrs={"class": "catalog_sale"})
Image = soup.find_all(attrs={"class": "catalog_item catalog_item_popup"})

connection = psycopg2.connect(host='localhost', dbname='FHWDB', user='postgres', password='Q1w2e3r4')
cursor = connection.cursor()
create_q = '''CREATE TABLE Parse  
     (ID serial primary key, Name varchar(100), Price varchar(9), Discount varchar(10), src varchar(110))'''
cursor.execute(create_q)
connection.commit()

for j in range(60):
    url = 'https://flawery.ru'+Image[j].find('a').find('picture').find('img').attrs['src']
    tempf = f"C:\\Users\\user\\PFDB{j}.jpg"
    wget.download(url, tempf)
    insert_query = f'''INSERT into public.Parse(Name, Price, Discount, src) values ('{Name[j].text}', '{Price[j].text}', '{Discount[j].text}', '{tempf}') '''
    cursor.execute(insert_query)
connection.commit()

cursor.execute("SELECT * from Parse")
print(cursor.fetchall())

cursor.close()
connection.close()
