import telebot
import os

TOKEN = os.getenv('TELE_TOKEN') # чувствительные данные прячем
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    # start_btn = telebot.types.KeyboardButton("/start")
    help_btn = telebot.types.KeyboardButton("/help")
    markup.add(help_btn)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, '@xzectlitakoiadres')  # кидает ссылку на тех.п. к примеру


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    msg = message.text
    bot.send_message(message.from_user.id, msg)



bot.polling(none_stop=True, interval=0)