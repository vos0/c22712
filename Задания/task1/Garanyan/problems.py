import psycopg2
import wget

from Задания.task1.Garanyan import parser

connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres',
                              password='Q1w2e3r4')
cursor = connection.cursor()
create_q = '''CREATE TABLE Food  
     (ID serial primary key, Name varchar(500), Price varchar(60), src varchar(100))'''

try:
    cursor.execute(create_q)
    connection.commit()
except psycopg2.errors.DuplicateTable:
    print("s")

for j in range(15):
    url = parser.Image[j].find('img').attrs['src']
    tempf = f"C:\\Users\\Harutyun\\Desktop\\prog\\food{j}.jpg"
    wget.download(url, tempf)
    try:
        insert_query = f'''INSERT into public.Food(Name, Price, src) values ('{parser.Name[j].text}', '{parser.Price[j].text}', '{tempf}') '''
        cursor.execute(insert_query)
        connection.commit()
    except:
        connection.rollback()

cursor.close()
connection.close()