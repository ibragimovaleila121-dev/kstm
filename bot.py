import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
TOKEN = "8728346342:AAHYmH1SkL5pBLiDGCXWVkj7cOmhFOj_JX8"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    # Создаём кнопку
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Перейти на сайт", url="https://voluble-babka-423657.netlify.app")
    keyboard.add(button)
    # Отправляем сообщение с кнопкой
    bot.send_message(message.chat.id, "Добро пожаловать! Нажми на кнопку:", reply_markup=keyboard)
print("Бот запущен")
bot.infinity_polling()