# coding=utf-8

import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from pprint import pprint

import time
import datetime
import sys

token_bot = '1006213300:AAF2FS_AXRJCLHWnZf1pI1TzuDxlRqJc2O4'

bot = telepot.Bot(token_bot)

def options_menu(chat_id):
    markup = ReplyKeyboardRemove()

    keyboard_option = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Informazioni', callback_data='help')
        ]
    ])

    bot.sendMessage(chat_id, 'Impostazioni', reply_markup=keyboard_option)

def create_password(chat_id, msg):

    bot.sendMessage(chat_id, "quanto vuoi che sia lunga la password?")

    print('test')

    bot.sendMessage(chat_id, "Sono ancora in fase di sviluppo")


def client_log(chat_id, msg):
    #Date = "Date:", datetime.datetime.today()
    #Time = "Time:", datetime.datetime.now()

    format_log = msg['date']['chat_id']['username']['text']

    time.sleep(5)
    
    log = open("log_bot.txt", "w+")
        
    log.write(str(format_log))

    log.close()

def help():
    pass

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Crea la tua password', callback_data='pwdgen'),
        InlineKeyboardButton(text='Impostazioni', callback_data='options_menu')]
        ])

    bot.sendMessage(chat_id, 'Benvenuto su pwd generator', reply_markup=keyboard)

    #client_log(chat_id, msg)

def on_callback_query(msg):
    query_id, chat_id, query_data, = telepot.glance(msg, flavor='callback_query')

    if query_data == 'pwdgen':
        create_password(chat_id, msg)
    elif query_data == 'options_menu':
        options_menu(chat_id)
    elif query_data == 'help':
        help()

print ('Listening ...')

MessageLoop(bot,
    {
        'chat':on_chat_message,
        'callback_query': on_callback_query
    }
).run_as_thread()

while True:
    time.sleep(10)