#!/usr/bin/python
# -*- coding: utf8 -*-

# ============================================================
# Description: edu project for BeautifulSoup learning.
# https://habr.com/ru/sandbox/132503/ 
# ============================================================-

import sys, traceback
from bs4 import BeautifulSoup
import requests

url = 'http://mignews.com/mobile'
new_news = []
news = []

# main entrance point:
if __name__ == "__main__":

    print "Main program begins"
    print ""

    try:
        page = requests.get(url)
        print (page.status_code)
        soup =BeautifulSoup(page.text, "html.parser")
        # print (soup)
        news = soup.findAll('a', class_ = 'lenta')
        # print (news)

        for i in range(len(news)):
            if news[i].find('span', class_='time2 time3') is not None:
                new_news.append(news[i].text)

        for i in range(len(new_news)):
            print(new_news[i])        

        print "App complete."
    except:
        traceback.print_exc()
        # self.log.saveMessageToLog(a)
        print "Trigger Exception, traceback info forward to log file."
        traceback.print_exc(file=open("errlog.txt","a"))
        sys.exit(1) 

    print ""
    print "Main program ends"


