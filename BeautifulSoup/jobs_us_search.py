#!/usr/bin/python
# -*- coding: utf8 -*-

# ============================================================
# Description: edu project for BeautifulSoup learning.
# https://habr.com/ru/sandbox/134528/ 
# ============================================================-

import sys, traceback
from bs4 import BeautifulSoup
import requests

URL_TEMPLATE = 'https://www.work.ua/ru/jobs-odesa/?page=2'
FILE_NAME = "test.csv"

def parse(url = URL_TEMPLATE):
    result_list = {'href': [], 'title': [], 'about': []}
    r = requests.get(url)
    # return 1

    soup = BeautifulSoup(r.text, "html.parser")
    #print soup
    #return 1

    vacancies_names = soup.find_all('h2', class_='add-bottom-sm')
    vacancies_info = soup.find_all('p', class_='overflow')
    for name in vacancies_names:
        result_list['href'].append('https://www.work.ua'+name.a['href'])
        result_list['title'].append(name.a['title'])
    for info in vacancies_info:
        result_list['about'].append(info.text)
    print result_list

    return result_list


# main entrance point:
if __name__ == "__main__":

    print "Main program begins"
    print ""

    try:        
        data = parse()

        print "App complete."
    except:
        traceback.print_exc()
        # self.log.saveMessageToLog(a)
        print "Trigger Exception, traceback info forward to log file."
        traceback.print_exc(file=open("errlog.txt","a"))
        sys.exit(1) 

    print ""
    print "Main program ends"



#===========================================
# import requests
# from bs4 import BeautifulSoup as bs
# import pandas as pd

# URL_TEMPLATE = "https://www.work.ua/ru/jobs-odesa/?page=2"
# FILE_NAME = "test.csv"


# def parse(url = URL_TEMPLATE):
    # result_list = {'href': [], 'title': [], 'about': []}
    # r = requests.get(url)
    # soup = bs(r.text, "html.parser")
    # vacancies_names = soup.find_all('h2', class_='add-bottom-sm')
    # vacancies_info = soup.find_all('p', class_='overflow')
    # for name in vacancies_names:
        # result_list['href'].append('https://www.work.ua'+name.a['href'])
        # result_list['title'].append(name.a['title'])
    # for info in vacancies_info:
        # result_list['about'].append(info.text)
    # return result_list
# 
# 
# df = pd.DataFrame(data=parse())
# df.to_csv(FILE_NAME)
