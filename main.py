import telebot
import requests, json
from telebot import types

API_KEY = "ca0cca3938bb8543f78af4199b823832"
TELEGRAM_API_KEY = "6125794533:AAHxwStb0LJZicd7OVcLUFXDYvwGSJ91oUc"
bot = telebot.TeleBot(TELEGRAM_API_KEY)
def weather_temp(message, city, API_KEY):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL = BASE_URL + "q=" + city + "&appid=" + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        temperature = int(data['main']['temp'] - 273.15)
        return temperature
    else:
        bot.send_message(message.chat.id, "\U0001F92D")

def weather_desc(message, city, API_KEY):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL = BASE_URL + "q=" + city + "&appid=" + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        desc = data['weather'][0]['description']
        return desc
    else:
        bot.send_message(message.chat.id, "\U0001F92D")


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton("Вінниця")
    url_button1 = types.InlineKeyboardButton(text="прогноз", url="https://sinoptik.ua/погода-винница/10-дней")
    markup.add(button1)
    markup.add(url_button1)
    bot.send_message(message.chat.id, "Привіт, {0.first_name}! Натисни на кнопку)".format(message.from_user), reply_markup=markup)
    msg = bot.reply_to(message, "Привіт! Я бот який показує погоду \U0001F31E по місту.")
    bot.send_message(message.chat.id, "Веди назву міста, щоб побачити температуру")
    bot.register_next_step_handler(msg, print_weather)



def print_weather(message):
    city = message.text
    temperature = weather_temp(message,city, API_KEY)
    description = weather_desc(message,city, API_KEY)
    if city == "прогноз":
        bot.send_message(message.chat.id, "https://sinoptik.ua/погода-винница/10-дней")
    if temperature == None:
        str = "Помилка в написані"
    else:
        bot.send_message(message.chat.id, "\U0001F321")
        str = "Температура \U0001F321 " + f" : {temperature}°C" + "\n"+f"В загальному {description}"
        if temperature > 15:
            bot.send_message(message.chat.id, "\U0001F31E")
        else:
            bot.send_message(message.chat.id, "\U00002601")
    msg = bot.reply_to(message, str)
    bot.send_message(message.chat.id, "Веди назву міста, щоб продовжити")
    bot.register_next_step_handler(msg, print_weather)

def weather_desc(message, city, API_KEY):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL = BASE_URL + "q=" + city + "&appid=" + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        desc = data['weather'][0]['description']
        return desc
    else:
        bot.send_message(message.chat.id, "\U0001F92D")


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton("Вінниця")
    markup.add(button1)
    bot.send_message(message.chat.id, "Привіт, {0.first_name}! Натисни на кнопку)".format(message.from_user), reply_markup=markup)
    msg = bot.reply_to(message, "Привіт! Я бот який показує погоду \U0001F31E по місту.")
    bot.send_message(message.chat.id, "Веди назву міста, щоб побачити температуру")
    bot.register_next_step_handler(msg, print_weather)


def weather_for5(message, city, API_KEY):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL = BASE_URL + "q=" + city + "&appid=" + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        bot.send_message(message.chat.id,data['weather'][0]['description'])
    else:
        bot.send_message(message.chat.id, "\U0001F92D")


bot.polling()