import telebot
import psycopg2
def execute_request(request):
    connection = psycopg2.connect(host='localhost', dbname='dbdata',
                              user='postgres', password='Q1w2e3r4')
    cursor = connection.cursor()
    cursor.execute(request)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
min_id = int(execute_request("select min(id) from parsing")[0][0])
max_id = int(execute_request("select max(id) from parsing")[0][0])
bot = telebot.TeleBot('6060681334:AAHASvjmAEn_DF_NjymP1MMpq14kYx_2cZw')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, f'Привет. Введите идентификатор от {min_id} до {max_id}, чтобы получить данные: ')
@bot.message_handler(content_types=["text"])
def from_bd(message):
    try:
        current_id = int(message.text)
    except BaseException:
        bot.send_message(message.chat.id, "Вы неправильно ввели ID. Попробуйте снова:")
        return
    if current_id > max_id or current_id < min_id:
        bot.send_message(message.chat.id, "ID больше, чем количество товаров. Попробуйте снова:")
        return
    else:
        data = execute_request(f"select * from parsing where id = {current_id}")[0][1:]
        names_of_columns = ["name", "link"]
        everydata = []
        for data_name, column_name in zip(data, names_of_columns):
            everydata.append(column_name.capitalize() + ": " + data_name)
        bot.send_message(message.chat.id, "\n\n".join(everydata))
    bot.send_message(message.chat.id, f"Введите следующий ID от {min_id} до {max_id}:")
bot.polling(none_stop=True, interval=0)
#for commit
