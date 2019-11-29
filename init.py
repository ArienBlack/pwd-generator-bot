# coding=utf-8

import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from pprint import pprint

import time
import datetime
import sys
import logging
import emoji
import random

token_bot = '1006213300:AAF2FS_AXRJCLHWnZf1pI1TzuDxlRqJc2O4'

bot = telepot.Bot(token_bot)

def options_menu(chat_id):
    time.sleep(1)

    keyboard_option = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=emoji.emojize(':page_facing_up: Informazioni', use_aliases=True), callback_data='help')
        ]
    ])

    bot.sendMessage(chat_id, 'Impostazioni', reply_markup=keyboard_option)

def create_password(chat_id, msg):
    time.sleep(1)

    d = datetime.date.today()
    current_date = d.strftime("%d-%m-%Y")

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    charset = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

    pwd_generated = ''.join(random.choice(charset) for x in range(12))

    print(pwd_generated)

    bot.sendMessage(chat_id, pwd_generated)

    bot.sendMessage(chat_id, f"Password generata il {current_date}, alle {current_time}")

    bot.sendMessage(chat_id, "Ehy ricordati che sono ancora in fase di sviluppo")

def client_log(chat_id, msg):
    message = msg['text']

    logging.basicConfig(filename="bot_log.txt", level=logging.DEBUG, format='["%(asctime)s", %(message)s]')

    logging.info(f'Chat_id: {chat_id}, Message: {message}')

def help(chat_id):
    bot.sendMessage(chat_id, """Autore: Arien01, 
    Privacy: Il bot genera in maniera autonoma e diversa da ogni altra le chiavi donate all'utente. All'interno del bot non vi è alcuna funzione per il salvataggio delle password.
    """)

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    time.sleep(1)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=emoji.emojize(':key: Genera password', use_aliases=True), callback_data='pwdgen'),
        InlineKeyboardButton(text=emoji.emojize(':wrench: Impostazioni', use_aliases=True), callback_data='options_menu')]
        ])

    bot.sendMessage(chat_id, 'Benvenuto su pwd generator', reply_markup=keyboard)

    client_log(chat_id, msg)

def on_callback_query(msg):
    query_id, chat_id, query_data, = telepot.glance(msg, flavor='callback_query')

    if query_data == 'pwdgen':
        create_password(chat_id, msg)
    elif query_data == 'options_menu':
        options_menu(chat_id)
    elif query_data == 'help':
        help(chat_id)

print ('Listening ...')

MessageLoop(bot,
    {
        'chat':on_chat_message,
        'callback_query': on_callback_query
    }
).run_as_thread()

while True:
    time.sleep(10)