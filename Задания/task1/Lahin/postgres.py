import psycopg2
import wget
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
i = 1
s = Service("С:\DATA\ChromeDriver\chromedriver.exe")
browser = webdriver.Chrome(service=s)
browser.get("https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118?from=under_search")
height = browser.execute_script("return document.body.scrollHeight")
time.sleep(4)
while 900*i < height:
    height = browser.execute_script("return document.body.scrollHeight")
    browser.execute_script(f"window.scrollTo(0,{900*i})")
    time.sleep(1)
    i+=1
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
productst = soup.find_all('a', class_="product-title__text")
pricest = soup.find_all('span', class_="price__main-value")
features = soup.find_all('ul', class_="product-feature-list product-feature-list--undefined")
pictures =  soup.find_all('img', class_="product-picture__img product-picture__img--list")
products, prices, diagonals, resolutions, CPUs, RAMs, Graphics_controllers, Volumes = [],[],[],[],[],[],[],[]
for i in range(len(productst)):
    products.append(productst[i].text.strip())
    prices.append(pricest[i].text.replace("\xa0", "").strip())
for feature in features:
    u = feature.text
    diagonals.append(u[20:u.find("\"",20)+1])
    resolutions.append(u[u.find("\"",20)+2:u.find(".", 23)+1])
    CPUs.append(u[u.find("Процессор",20)+9:u.find("ГГц",20)+3].replace("\xa0",""))
    RAMs.append(" ".join(u[u.find("(RAM)",20)+5:u.find("Графический контроллер")].split()))
    Graphics_controllers.append(u[u.find("Графический контроллер")+22:u.rfind("Объем")-2])
    Volumes.append(u[u.rfind("Объем")+6:].replace("\xa0", "").strip())
for i in range(len(Volumes)):
    u = Volumes[i]
    if u.rfind("D")!=-1: Volumes[i] = u[:u.rfind("D")+1]+ " " + u[u.rfind("D")+1:]
    else: Volumes[i] = u[:u.rfind("С")+1]+ " " + u[u.rfind("С")+1:]
connection=psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4')
cursor = connection.cursor()
insert = """CREATE TABLE public.laptops(
id serial primary key,
product varchar(100),
price varchar(15),
diagonal varchar(5),
resolution varchar(20),
CPU varchar(50),
RAM varchar(10),
Graphics_Controller varchar(40),
Volume varchar(25),
src varchar(100)
);
"""
cursor.execute(insert)
connection.commit()
for i in range(len(products)):
    url = "https://"+pictures[i]['src']
    filename = f"C:\DATA\Images\{i+1}.jpg"
    wget.download(url, filename)
    insert = f"""INSERT INTO public.laptops(
        product, price, diagonal, resolution, CPU, RAM, Graphics_Controller, Volume, src)
        VALUES
        ('{products[i]}', '{prices[i]}', '{diagonals[i]}', '{resolutions[i]}', '{CPUs[i]}', '{RAMs[i]}', '{Graphics_controllers[i]}', '{Volumes[i]}', '{filename}');"""
    cursor.execute(insert)
    connection.commit()
cursor.execute("select * from laptops")
print("Результат", cursor.fetchall())
cursor.close()
connection.close()

