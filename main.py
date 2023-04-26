import telebot
from telebot import types

bot = telebot.TeleBot("6125794533:AAHxwStb0LJZicd7OVcLUFXDYvwGSJ91oUc")

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.reply_to(message, "Hello, I'm a recipe bot. What recipe would you like to find?")

bot.polling()
