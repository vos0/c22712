from bs4 import BeautifulSoup        # подключение к библиотекам парсинга и работы с базами данных
import psycopg2
from wget import download
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

S = Service("D:\Драйвер\chromedriver.exe")
browser = webdriver.Chrome(service=S)
browser.get('https://ultrasport.ru/catalog/velosipedy/gornye_velosipedy/')   # подключение к сайту, с которого будем парсить данные
html_text = browser.page_source       # сохранение html кода страницы в переменную html_text
soup = BeautifulSoup(html_text, 'lxml')         # преобразуем код в дерево объектов

info = soup.find_all('div', class_="inner_wrap TYPE_1")  # поиск всех описывающих товар общих тэгов

try:
    connection = psycopg2.connect(                  # подключение к базе данных
        host='localhost',
        dbname='Bicycles',
        user='postgres',
        password='Q1w2e3r4'
    )
    connection.autocommit = True                    # настройка автоматического комита

    with connection.cursor() as cursor:             # создание таблицы в базе данных
        cursor.execute(
            """CREATE TABLE bikes(
            id serial PRIMARY KEY,
            bike_name varchar(100) NOT NULL,
            bike_view varchar(1000) NOT NULL,
            bike_price varchar(100) NOT NULL,
            bike_availability varchar(100) NOT NULL);
            """
        )
    with connection.cursor() as cursor:          # заполнение таблицы данным, которые мы спарсили с сайта
        for i, item in enumerate(info):
            name = item.find('a', class_="dark_link js-notice-block__title option-font-bold font_sm").text.strip()
            price = item.find('div', class_="price only_price font-bold font_mxs").text.strip()
            enough = item.find('span', class_="value font_sxs").text.strip()
            p_src = item.find('img', class_="lazy img-responsive").get("src")
            download(p_src, f"images/{i+1}.jpg")
            cursor.execute(
                f"""INSERT INTO public.bikes(
                bike_name, bike_view, bike_price, bike_availability)
                VALUES
                ('{name}','images/{i+1}.jpg','{price}','{enough}');"""
            )


except Exception as _ex:                     # обработка ошибок
    print("[INFO] ERROR", _ex)

finally:                                      # завершение подключения
    if connection:
        connection.close()
        print("[INFO] Connection closed")

