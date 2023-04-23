import psycopg2

connection = psycopg2.connect(host='localhost', dbname='FHWDB', user='postgres', password='Q1w2e3r4')
cursor = connection.cursor()

def edit(Col, N, NN, value):#Функция внесения изменений и сортировки
    upd_query = f'''UPDATE Parse SET {Col} = '{NN}' WHERE {Col} = '{N}' '''
    cursor.execute(upd_query)
    ord_query = f'''SELECT * FROM public.parse order by {value};'''
    cursor.execute(ord_query)
    connection.commit()

edit('Name', 'Ирисы небесно-голубого цвета', 'Ирисы', 'ID')

#print(cursor.fetchall()) - для проверки

def select(ID):
    s_query = f'''SELECT * FROM public.Parse where ID = {ID}'''
    cursor.execute(s_query)
    return cursor.fetchone()

#print(select(44)) - для проверки
