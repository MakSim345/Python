#!/usr/bin/python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

# ============================================================
# Description: edu project for BeautifulSoup learning.
# https://habr.com/ru/sandbox/132503/ 
# ============================================================-

import sys, traceback
from bs4 import BeautifulSoup
import requests


def getTheNews():
    
    url = 'http://mignews.com/mobile'
    new_news = []
    news = []
    retStr = ""

    page = requests.get(url)
    print ("Server response:", page.status_code)
    soup =BeautifulSoup(page.text, "html.parser")
    # print (soup)
    news = soup.findAll('a', class_ = 'lenta')
    # print (news)

    for i in range(len(news)):
       if news[i].find('span', class_='time2 time3') is not None:
           new_news.append(news[i].text)

    for i in range(len(new_news)):
       # print(new_news[i])        
       retStr = retStr + new_news[i] + "\n"        
    
    # print retStr
    # text_to_send = getTheNews().encode('utf-8')
    return retStr

# main entrance point:
if __name__ == "__main__":
    #ENCODE_STR = 'utf-8'
    ENCODE_STR = 'UTF-8'
    # ENCODE_STR = 'cp-1251'

    try:
        print "Main program begins"
        print ""
        text_to_print = getTheNews().encode(ENCODE_STR)
        #text_to_print = getTheNews().encode()
        print text_to_print   
    except:
        traceback.print_exc()
        # self.log.saveMessageToLog(a)
        print "Trigger Exception, traceback info forward to log file."
        traceback.print_exc(file=open("errlog.txt","a"))
        sys.exit(1) 

    print ""
    print "Main program ends"


