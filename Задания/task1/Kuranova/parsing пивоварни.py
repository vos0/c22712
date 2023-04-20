from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import psycopg2
from time import sleep
s = Service("C:\data\chromedriver.exe")
browser = webdriver.Chrome(service=s)
browser.get('https://untappd.com/brewery/top_rated')
sleep(1)
html_text=browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
ratings = soup.find_all('div', class_='beer-item')
item = []
for i in ratings:
    c = i.text
    c = c.split('\n')
    for k in c:
        if k == '':
            c.pop(c.index(k))
    d = i.find('img').get('src')
    c.append(d)
    item.append(c)
item.pop(3)
item.pop(8)


connection = psycopg2.connect(host='localhost', dbname='breweries', user='postgres', password='Q1w2e3r4t5')
cursor=connection.cursor()
create = """ create table Information
    (id int primary key, Name varchar(100), Place varchar(150), Sorts varchar(15), AmountOfRatings varchar(25),
    Rating varchar(10), ImageLink varchar(150));"""
cursor.execute(create)
connection.commit()
for i in range(20):
    insert_qwery="""INSERT INTO public.Information(id,Name, Place, Sorts, AmountOfRatings, Rating, ImageLink) VALUES
    ( '"""+str(i+1)+"""', '"""+item[i][0]+"""', '"""+item[i][1]+"""', '"""+item[i][2]+"""', '"""+item[i][3]+"""', 
    '"""+item[i][9]+"""', '"""+item[i][13]+"""');""";
    cursor.execute(insert_qwery)
    connection.commit()
cursor.execute('select * from Information')
print(cursor.fetchall())
cursor.close()
connection.close()
