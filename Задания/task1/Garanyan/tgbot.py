import telebot
import psycopg2
from telebot import types
import random
#hello
connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres',
                              password='Q1w2e3r4')
cursor = connection.cursor()
try:
    sel_query = """SELECT * FROM public.food"""
    cursor.execute(sel_query)
except psycopg2.errors.UndefinedTable:
    connection.rollback()
    import tableCreator

    sel_query = """SELECT * FROM public.food"""
    cursor.execute(sel_query)

array = list(cursor.fetchall())

bot = telebot.TeleBot('841097550:AAFc5MoFRivTEfv-gOSJctqH53NfYMTKpCc')


@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Хот-доги и соусы!")
    item2 = types.KeyboardButton("Повтори!")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id,
                     '"Хот-доги и соусы!" - для получения случайного товара из нашей хотдожной\n "Повтори!" - для повторения сообщений.',
                     reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if (message.text.strip() == 'Хот-доги и соусы!'):
        i = random.choice(array)
        ans = f'Название: {i[1]}\nЦена: {i[2]}\n'
        bot.send_message(message.chat.id, ans)
        bot.send_photo(message.chat.id, open(i[3], 'rb'))
    elif (message.text.strip() == 'Повтори!'):
        bot.send_message(message.chat.id, 'Ввод: ' + message.text)


bot.polling(none_stop=True, interval=0)