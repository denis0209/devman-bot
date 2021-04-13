import telegram
bot = telegram.Bot(token='1620299649:AAGWjR7VqGz4kDnldm8Vt65_BcQIKr6jCnQ')

from telegram.ext import Updater
updater = Updater(token='1620299649:AAGWjR7VqGz4kDnldm8Vt65_BcQIKr6jCnQ', use_context=True)

dispatcher = updater.dispatcher

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def Start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Выберите автомобиль: \n/Mercedes \n/Audi \n/BMW \n/Ferrari \n/Toyota ")
def Mercedes(message):
    img = open('images/mercedes.jpg', 'rb')
    bot.send_photo(message.chat.id, img)
def Second(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Второй ответ")
def Third(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Третий ответ")

from telegram.ext import CommandHandler
start_handler = CommandHandler('Start', Start)
dispatcher.add_handler(start_handler)
start_handler = CommandHandler('Mercedes', Mercedes)
dispatcher.add_handler(start_handler)
start_handler = CommandHandler('Second', Second)
dispatcher.add_handler(start_handler)
start_handler = CommandHandler('Third', Third)
dispatcher.add_handler(start_handler)
updater.start_polling()

import os 

if __name__ == '__main__':
  Start()
  Mercedes()



password = os.getenv("PASSWORD")

print("Тайный пароль:")
print(password)

