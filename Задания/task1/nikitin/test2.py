from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import psycopg2
import wget
import time

connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4')
cursor = connection.cursor()

s = Service('D:\Games\data\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.volkswagen.ru/polo/')
html_text = browser.page_source
time.sleep(2)
soup = BeautifulSoup(html_text, 'lxml')

creat_table = """ create table Cars_volks
    (id serial primary key, car_name varchar(20),
    price varchar(15), adress varchar(300),
    scr varchar(150)) """
#cursor.execute(creat_table)
connection.commit()

car_names = soup.find_all('div', class_='avn001-2_name')
prices = soup.find_all('div', class_='avn001-2_price-container')
adresses = soup.find_all('div', class_='avn001-2_dealer-link__text')
pictures = soup.find_all('div', class_='avn001-2_image image__container')

for i in range(len(car_names)):
    url = pictures[i].find('img')['src']
    filename = f"C:\\Users\\Пользователь\\OneDrive\\Рабочий стол\\pycharm\\c22712\\Задания\\task1\\nikitin\\img\{i}.jpg"
    wget.download(url, filename)
    insert_qwery = f"""INSERT INTO public.Cars_volks(car_name, price, adress, scr)
    	VALUES ('{car_names[i].text}', '{prices[i].text}', '{adresses[i].text}', '{filename}')""";
    #cursor.execute(insert_qwery)
    connection.commit()

cursor.close()
connection.close()