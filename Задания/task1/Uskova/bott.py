import telebot
import random
from telebot import types
f = open('C:\\Users\\Yekaterina\\Desktop\\бот\\pisateli.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
f = open('C:\\Users\\Yekaterina\\Desktop\\бот\\facts.txt', 'r', encoding='UTF-8')
thinks  = f.read().split('\n')
f.close()
bot = telebot.TeleBot('6205726630:AAF4zfV_P2b0f7bClm__sWuRmoZ1XpiC_xo')
@bot.message_handler(commands=["start"])
def start(m, res=False):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Писатели")
        item2=types.KeyboardButton("Факты")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Нажми: \nПисатель'
        ' для получения интересного факта о писателе\nФакт '
        '— для получения факта о книгах ',  reply_markup=markup)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Писатели' :
            answer = random.choice(facts)
    elif message.text.strip() == 'Факты':
            answer = random.choice(thinks)
    bot.send_message(message.chat.id, answer)
bot.polling(none_stop=True, interval=0)
