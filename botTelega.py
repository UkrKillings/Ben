import telebot
from random import SystemRandom

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(command=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет, я Бен задавай вопросы:)')

@bot.message_handler(content_types=["text", "voice"])
def handler_text(message):

    a = SystemRandom().choice(["Yes", "No", "HAHAHAHA", "Bee"])

    bot.send_message(message.chat.id, a )
    bot.send_message(message.chat.id, "Путин хуйло!")

bot.polling(none_stop=True, interval=0)