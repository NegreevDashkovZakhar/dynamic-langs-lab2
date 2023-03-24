import telebot
import API_KEY
from controller.marksController import MarksController

API_TOKEN = API_KEY.api_key

bot = telebot.TeleBot(API_TOKEN)
marks_controller = MarksController()


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Здравствуйте! Я Марк Маркович и я могу помочь вам получить информацию об успеваемости ребенка.
""")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, marks_controller.parse_message(message.text))


bot.infinity_polling()
