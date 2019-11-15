#!/usr/bin/env python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

#############################################################################
##
## Info:
##
#############################################################################

import time
import sys
import telebot

import json
import requests

from telegram_auth import user_token

u_token = user_token()
TOKEN = u_token.token

URL = "https://api.telegram.org/bot{}/".format(TOKEN)

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): #
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)
