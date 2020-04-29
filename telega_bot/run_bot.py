#!/usr/bin/env python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

#############################################################################
##
## Info:
## https://www.codementor.io/garethdwyer/building-a-telegram-bot-using-python-part-1-goi5fncay
##
#############################################################################

import traceback
import socket
import struct
import time
import sys, os
import telebot

from platform import system
from telegram_auth import user_token
from news_from_izrael import getTheNews

sys.path.insert(0, '/home/ys/dev/scripts/weather_sms')
from weather_unit import weather_city

u_token = user_token()
TOKEN = u_token.token

URL = "https://api.telegram.org/bot{}/".format(TOKEN)

bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=['start'])
# def start_message(message):
#    bot.send_message(message.chat.id, "Привет, ты написал мне /start")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # DEBUG: 
    #print "get_text_message - enter:", message.text.lower()
    #print "get_text_message - enter: " + str(message.chat.id)
    if message.text.lower() == "/help":
        bot.send_message(message.chat.id, get_help())
    elif message.text.lower()  == "/start":
        bot.send_message(message.chat.id, "Привет, ты написал мне /start")
    elif message.text.lower()  == "time":
        bot.send_message(message.chat.id, get_timestamp())
    elif message.text.lower()  == 'Hello':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower()  == 'Bye':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower()  == 'ip':
        bot.send_message(message.chat.id, get_ip_address())
    elif message.text.lower()  == 'news':
        bot.send_message(message.chat.id, get_news())
    elif message.text.lower()  == 'whki':
        bot.send_message(message.chat.id, get_weather('helsinki'))
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю. Напиши /help.")

def get_help():
    return "Simple test: /start;\ntime - current timestamp;\nIP - server IP address;\nnews - news from Izrael;\nwhki - weather in Helsinki."

def get_news():
    text_to_send = getTheNews().encode('utf-8')
    return text_to_send

def get_local_os():
    local_os = system()
    if local_os == 'Linux':
        retValue = "OS - Linux"
    elif local_os == 'Windows':
        retValue = "OS - Windows. Module 'fcntl' not supported!"
    return retValue

def get_ip_address():
    ip_addr_list_to_send = "INFO: YS-SERVER " + time.strftime("%H:%M:%S %Y-%m-%d\n") + get_local_os()
    my_interfaces_list =  os.listdir('/sys/class/net/')
    for _network_if in my_interfaces_list:
        _ip_address = select_ip_address(_network_if)
        ip_addr_list_to_send = ip_addr_list_to_send + '\nIP address ' +_network_if +':\n' + _ip_address
    #end_for

    print ip_addr_list_to_send
    return ip_addr_list_to_send

def select_ip_address(ifname):
    local_os = system()
    if local_os == 'Linux':
        import fcntl
    elif local_os == 'Windows':
        # print "OS - Windows. Module 'fcntl' not supported!"
        return socket.gethostbyname(socket.gethostname())
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        retValue = socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15]))[20:24])
    except:
        retValue = "IP: "+ifname+" not exists!"

    return retValue

def get_weather(city_param='helsinki'):
    text_to_send = getTheNews().encode('utf-8')
    if city_param == 'helsinki':
        city_url = "http://www.foreca.com/Finland/Helsinki?tenday"
    else:
        city_url = "http://www.foreca.com/Ukraine/Dniprodzerzhyns%27k?tenday"

    try:
        weather = weather_city()
        weather.set_city_url(city_url)
        # weather.set_to_russian(False)
        weather_to_send = weather.get_weather_for_city()
    except:
        traceback.print_exc()
    return weather_to_send

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def get_timestamp(_selector = "date"):
    _day = time.strftime("%d")
    _year = time.strftime("%Y")
    _month = time.strftime("%m")

    # _date = _year + '-' +  self.mth_str.get_month(int(_month)) + '-' +  _day
    _date = _year + '-' +  _month + '-' +  _day
    _time = time.strftime("%H:%M:%S")

    if _selector == "time":
         return _time
    else:
        return _date + ' Time: '+ _time

if __name__ == '__main__':
    bot.infinity_polling(True)
    # bot.polling(none_stop=True)
    #bot.polling()

