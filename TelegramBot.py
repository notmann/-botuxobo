import telebot
import TOKEN
import random
 
from telebot import types
 
bot = telebot.TeleBot(TOKEN.TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    print('REGISTR_USER | ', message.chat.id, " |  {0.first_name}".format(message.from_user, bot.get_me()))
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Пить или не пить🍺")
    item2 = types.KeyboardButton("Работать🧑‍💻")
 
    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Пить или не пить🍺':
                alk = ['Пить🍺', 'Пить🥂', 'Пить🍷', 'Не пить','Пить🥃', 'Пить🍸', 'Пить🍹','Не пить!', 'Пить🧃']
                print('ПитьИлиНеПить')
                yes = bot.send_message(message.chat.id, random.choice(alk))

        elif message.text == 'Работать🧑‍💻':
            print('Работать')
            rad = random.randint(0,1)
            if rad == 0:
                yes = bot.send_message(message.chat.id, 'Работать🧑‍💻\nПереспроси еще раз :)')  
            if rad == 1:
                non = bot.send_message(message.chat.id, 'Не работать!')
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
 

# RUN
bot.polling(none_stop=True)