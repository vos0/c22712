import telebot
import psycopg2
from telebot import types
import random

connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4')

cursor = connection.cursor()

BD = """SELECT * FROM public.food"""
cursor.execute(BD)
array = list(cursor.fetchall())

bot = telebot.TeleBot('5696445699:AAEPKQgUAs39DTLr_iyQvlaFAsJNFK8DMnc')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рандомный товар")
    item2 = types.KeyboardButton("Повтор !")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id,
                     '"Рандомный товар" - для получения карточки товара\n "Повтори !" - для повторения сообщений.',
                     reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if (message.text.strip() == 'Рандомный товар'):
        i = random.choice(array)
        ans = f'Название: {i[1]}\nЦена: {i[2]}\nГрамм: {i[3]}\nРэйтинг: {i[4]}\n'
        bot.send_message(message.chat.id, ans)
    elif (message.text.strip() == 'Повтори !'):
        bot.send_message(message.chat.id, 'Ввод: ' + message.text)


bot.polling(none_stop=True, interval=0)