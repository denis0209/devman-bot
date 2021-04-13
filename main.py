import telegram
bot = telegram.Bot(token='1620299649:AAGWjR7VqGz4kDnldm8Vt65_BcQIKr6jCnQ')

from telegram.ext import Updater
updater = Updater(token='1620299649:AAGWjR7VqGz4kDnldm8Vt65_BcQIKr6jCnQ', use_context=True)

dispatcher = updater.dispatcher

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def Start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Список команд: \n/First \n/Second \n/Third")
def First(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Первый ответ")
def Second(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Второй ответ")
def Third(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Третий ответ")

from telegram.ext import CommandHandler
start_handler = CommandHandler('Start', Start)
dispatcher.add_handler(start_handler)
start_handler = CommandHandler('First', First)
dispatcher.add_handler(start_handler)
start_handler = CommandHandler('Second', Second)
dispatcher.add_handler(start_handler)
start_handler = CommandHandler('Third', Third)
dispatcher.add_handler(start_handler)
updater.start_polling()

import os 

password = os.getenv("PASSWORD")

print("Тайный пароль:")
print(password)