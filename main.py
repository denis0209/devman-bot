import telegram
bot = telegram.Bot(token='1620299649:AAGWjR7VqGz4kDnldm8Vt65_BcQIKr6jCnQ')

from telegram.ext import Updater
updater = Updater(token='1620299649:AAGWjR7VqGz4kDnldm8Vt65_BcQIKr6jCnQ', use_context=True)

dispatcher = updater.dispatcher

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def Start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Выберите автомобиль: \n/Mercedes \n/Audi \n/BMW \n/Ferrari \n/Toyota \n/Renault \n/Nissan \n/KIA")
def Mercedes(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Mercedes-Benz — торговая марка и одноимённая компания — производитель легковых автомобилей премиального класса, грузовых автомобилей, автобусов и других транспортных средств, входящая в состав немецкого концерна «Daimler AG». Является одним из самых узнаваемых автомобильных брендов во всём мире.")
def Audi(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Audi AG — немецкая автомобилестроительная компания в составе концерна Volkswagen Group, специализирующаяся на выпуске автомобилей под маркой Audi. Штаб-квартира расположена в городе Ингольштадт. Девиз — Vorsprung durch Technik. Объём производства в 2016 году составил около 1 903 259 автомобилей.")
def BMW(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="BMW AG — немецкий производитель автомобилей, мотоциклов, двигателей, а также велосипедов. Председателем компании с 2006 по 2015 год был Норберт Райтхофер, с мая 2015 года — Харальд Крюгер, а с 18 июля 2019 года — Оливер Ципсе. Главный дизайнер — Йозеф Кабан.")
def Ferrari(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ferrari NV — итальянская компания, выпускающая спортивные и гоночные автомобили, базирующаяся в Маранелло. Основана в 1947 году Энцо Феррари как Scuderia Ferrari, компания спонсировала гонщиков и производила гоночные машины до 1947 года.")
def Toyota(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Toyota Motor Corporation — крупнейшая японская автомобилестроительная корпорация, также предоставляющая финансовые услуги и имеющая несколько дополнительных направлений в бизнесе. Является крупнейшей автомобилестроительной публичной компанией в мире, а также крупнейшей публичной компанией в Японии.")
def Renault(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Renault Group — французская автомобилестроительная корпорация. Штаб-квартира компании расположена в городе Булонь-Бийанкуре, недалеко от Парижа. Входит в Альянс Renault–Nissan–Mitsubishi")
def Nissan(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Nissan Motor Co., Ltd. — японский автопроизводитель, один из крупнейших в мире. Компания основана в 1933 году. По состоянию на 2010 год занимает 8-е место в мировом рейтинге автопроизводителей по версии международного института исследования рынка IHS Automotive. Штаб-квартира находится в городе Иокогама.")
def KIA(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Kia Motors Corporation — южнокорейская автомобилестроительная компания, второй автопроизводитель в Республике Корея и седьмой в мире, основана в декабре 1944 года. Входит в группу компаний Hyundai Motor Group. В 2016 году в мире было продано 3 007 976 автомобилей. Официальный слоган компании — «The Power to Surprise».")



from telegram.ext import CommandHandler
start_handler = CommandHandler('Start', Start)
dispatcher.add_handler(start_handler)
start_handler = CommandHandler('Mercedes', Mercedes)
dispatcher.add_handler(start_handler)
start_handler = CommandHandler('Audi', Audi)
dispatcher.add_handler(start_handler)
start_handler = CommandHandler('BMW', BMW)
dispatcher.add_handler(start_handler)
start_handler = CommandHandler('Ferrari', Ferrari)
dispatcher.add_handler(start_handler)
start_handler = CommandHandler('Toyota', Toyota)
dispatcher.add_handler(start_handler)
start_handler = CommandHandler('Nissan', Nissan)
dispatcher.add_handler(start_handler)
start_handler = CommandHandler('KIA', KIA)
dispatcher.add_handler(start_handler)
updater.start_polling()

import os 

password = os.getenv("PASSWORD")

print("Тайный пароль:")
print(password)

