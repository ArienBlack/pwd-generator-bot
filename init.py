import telepot
from pprint import pprint
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

import time
import datetime
import sys

token_bot = '1006213300:AAF2FS_AXRJCLHWnZf1pI1TzuDxlRqJc2O4'

bot = telepot.Bot(token_bot)

def handle(msg):
    pprint(msg)

def options_menu(chat_id):
    markup = ReplyKeyboardRemove()

    keyboard_option = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Imposta la lunghezza della password', callback_data='pwd-lenght'),
        InlineKeyboardButton(text='Informazioni', callback_data='help')
    ]])

    
        #pwd_length = msg['']

    bot.sendMessage(chat_id, 'Working in progress', reply_markup=keyboard_option)

def create_password(chat_id):
    bot.sendMessage(chat_id, "Sono ancora in fase di sviluppo")

def client_log(chat_id, msg):
    format_log = [
        #"Date:",     datetime.date.today(),
        #"Hours:",    datetime.time.hour(),
        #"Minutes:",  datetime.time.minute(),
        "Chat_id:",  chat_id,
        "Message:",  msg,
        ]

    log = open("log_bot.txt", "w+")
    while True:
        log.write(str(format_log))

    log.close()

    #print(chat_id, msg)


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Crea la tua password', callback_data='pwdgen'),
        InlineKeyboardButton(text='Impostazioni', callback_data='options')]
        ])

    bot.sendMessage(chat_id, 'Benvenuto su pwd generator', reply_markup=keyboard)

    client_log(chat_id, msg)

def on_callback_query(msg):
    query_id, chat_id, query_data, = telepot.glance(msg, flavor='callback_query')

    if query_data == 'pwdgen':
        create_password(chat_id)
    elif query_data == 'options':
        options_menu(chat_id)

print ('Listening ...')

MessageLoop(bot,
    {
        'chat':on_chat_message,
        'callback_query': on_callback_query
    }
).run_as_thread()

while True:
    time.sleep(10)