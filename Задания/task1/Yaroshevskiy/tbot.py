import telebot as tb
import config
import psycopg2 as ps


def exec_query(query: str) -> list:
    with ps.connect(dbname=config.db_name, user=config.user) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            res = cur.fetchall()
    return res


def get_data(mess, bot, rows_number: int) -> None:
    try:
        product_id = int(mess.text)
    except BaseException:
        bot.send_message(mess.chat.id, "Invalid id")
        return

    if product_id > rows_number:
        bot.send_message(mess.chat.id, "Id is bigger than number of products")
        return
    else:
        data = exec_query(
            f"select * from images where id = {product_id}")[0][1:]

    bot.send_message(mess.chat.id, "\n\n".join(data))


bot = tb.TeleBot(config.token)

keyboard = tb.types.ReplyKeyboardMarkup()
keyboard.row("get data")


@bot.message_handler(commands=["start"])
def hi(mess):
    bot.send_message(mess.chat.id, "HI there!", reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def f(mess):
    if mess.text == "get data":
        row_number = int(exec_query("select count(*) from images")[0][0])
        bot.send_message(mess.chat.id, f"Write id between 1 and {row_number}")
        bot.register_next_step_handler(mess, get_data, bot, row_number)


bot.polling(non_stop=True)
