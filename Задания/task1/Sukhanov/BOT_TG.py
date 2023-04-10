import telebot
import random
from telebot import types

# Загружаем список интересных фактов
f = open('C:\\Users\\71332\\Desktop\\p\\факт.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
# Загружаем список поговорок
f = open('C:\\Users\\71332\\Desktop\\p\\поговорка.txt', 'r', encoding='UTF-8')
thinks  = f.read().split('\n')
f.close()

# Создаем экземпляр бота
bot = telebot.TeleBot('6293063008:AAEFscB5LEjxC_4irrcgT-z6Eb0NXYOxZng')

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):

    # Добавляем две кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Факт")
    item2 = types.KeyboardButton("Поговорка")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id, 'Нажми: \nФакт'
                                ' для получения интересного факта\nПоговорка '
                                '— для получения мудрой цитаты ', reply_markup=markup)

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])  #прослушиваем сообщения
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт
    if message.text.strip() == 'Факт':
        answer = random.choice(facts)
    # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == 'Поговорка':
        answer = random.choice(thinks)
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)

    #bot.send_message(message.chat.id, 'Вы написали: ' + message.text)

# Запускаем бота
bot.infinity_polling(none_stop=True, interval=0)   #запустить через DEBUG