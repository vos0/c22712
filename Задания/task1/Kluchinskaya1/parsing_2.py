from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from wget import download
import psycopg2
connection = psycopg2.connect(host='localhost', dbname='dbdata',
                              user='postgres', password='Q1w2e3r4')
cursor=connection.cursor()
s = Service('C:\\Users\\Dasha\\Desktop\\Progect\\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser = webdriver.Chrome()
url = 'https://www.tretyakovgallery.ru/'
browser.get(url)
html_text=browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
products = soup.find_all(attrs={"class": "building-item"})
for i, product in enumerate(products):
    link = product.find("img").attrs.get("src")
    tag = product.find("strong")
    name = product.find(attrs={"class": "building-item__title"})
    description = product.find(attrs={"class": "building-item__description"})
    if tag is not None:
        download(url + link, f"img\\{i}.jpg")
        cursor.execute(f"""INSERT INTO public.parsing(url, workhours, name, description, filename)
                          VALUES           
                          ( '{url + link}', '{tag.text}', '{name.text.strip()}', '{description.text.strip()}', 'img\\{i}.jpg')""")
connection.commit()
cursor.close()
connection.close()