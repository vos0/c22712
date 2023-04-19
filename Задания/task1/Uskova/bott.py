import telebot
import psycopg2
import config
from telebot import types
import random
import tableCreator

connection = psycopg2.connect(host='localhost', dbname='parc', user='postgres', password='Q1w2e3r4')
cursor = connection.cursor()

ins_query = """SELECT * FROM public.Notebooks"""
cursor.execute(ins_query)
array = list(cursor.fetchall())

bot = telebot.TeleBot('6205726630:AAF4zfV_P2b0f7bClm__sWuRmoZ1XpiC_xo')
@bot.message_handler(commands=["start"])

def start(m, res=False):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Выбери ноутбук")
        item2=types.KeyboardButton("Еще!")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Нажми: \nВыбери ноутбук'
        ' для просмотра товара\nЕще! '
        '— для повтора',  reply_markup=markup)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Выбери ноутбук' :
            q = random.choice(array)
            answer = f'Название: {q[1]}\nОписание: {q[2]}\nКод: {q[3]}\nЦена: {q[4]}\n'
            bot.send_message(message.chat.id, answer)
            bot.send_picture(message.chat.id, open(q[5], 'rb'))
    elif message.text.strip() == 'Еще!':
            bot.send_message(message.chat.id, 'Ввод: '+ message.text)
bot.polling(none_stop=True, interval=0)
