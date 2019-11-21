#!/usr/bin/python
# -*- coding: utf8 -*-

# ============================================================
# Description: edu project for BeautifulSoup learning.
# ============================================================-


import sys, traceback
from bs4 import BeautifulSoup
import requests
import urllib2

# url = "https://www.foreca.com/Finland/Helsinki?tenday"
url = 'https://www.foreca.com/Finland/Helsinki'
new_news = []
news = []

# main entrance point:
if __name__ == "__main__":

    print "Main program begins"
    print ""

    try:
        # page = requests.get(url)
        # print "Web Page respond:", page.status_code

        f = urllib2.urlopen(url)    
        page = f.read()
        # print "page: " , page

        soup =BeautifulSoup(page, "html.parser")
        print (soup)
        
        news = soup.findAll('a', class_ = 'h2')
        print (news)

        #for i in range(len(news)):
        #    if news[i].find('span', class_='time2 time3') is not None:
        #        new_news.append(news[i].text)

        #for i in range(len(new_news)):
        #    print(new_news[i])        

        print "App complete."
    except:
        traceback.print_exc()
        # self.log.saveMessageToLog(a)
        print "Trigger Exception, traceback info forward to log file."
        traceback.print_exc(file=open("errlog.txt","a"))
        sys.exit(1) 

    print ""
    print "Main program ends"


