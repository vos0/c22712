from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import psycopg2
import wget
import time

connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4')
cursor = connection.cursor()



s = Service('C:/Users/rusta/OneDrive/Рабочий стол/ИНФА/инфа 2 сем/driver/chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.kp.ru/expert/elektronika/luchshie-noutbuki/')
time.sleep (10)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')

creat_table="""create table notes
    (id serial primary key, name varchar(150),
    scr varchar(150))"""
cursor.execute(creat_table)
connection.commit()


names= soup.find_all('h3', class_="wp-block-heading")
pictures = soup.find_all('figure', class_="wp-block-image size-full")
print(len(names))
for i in range(len(names)):
    url = pictures[i].find('img')['src']
    filename = f"C:\\Users\\rusta\\OneDrive\\Рабочий стол\\pictures\\{i}.jpg"
    wget.download(url, filename)

    insert_qwery = """INSERT INTO public.notes(name, scr)
    VALUES( %s, %s, %s);"""
    record_to_insert = (names[i].text, filename)
    cursor.execute(insert_qwery, record_to_insert)
    connection.commit()

cursor.close()
connection.close()