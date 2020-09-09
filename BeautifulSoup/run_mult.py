#!/usr/bin/python
# -*- coding: utf8 -*-

# ============================================================
# Description: edu project for BeautifulSoup learning.
# ============================================================-


import sys, traceback
from bs4 import BeautifulSoup
import requests
import urllib3
from multiprocessing import Pool 

# from concurrent.futures import ThreadPoolExecutor

# url = "https://www.foreca.com/Finland/Helsinki?tenday"
url = 'http://www.foreca.fi/Finland/Helsinki'
new_news = []
news = []

def if_prime(x):
    if x <= 1:
        return 0
    elif x <= 3:
        return x    
    elif x % 2 == 0 or x % 3 == 0:
        return 0
    i = 5
    
    while i**2 <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return 0
        i += 6
    return x

# main entrance point:
if __name__ == "__main__":

    print "Main program begins"
    print ""
    
    answer = 0
    #with Pool(2) as pool_scrap:
    #    answer = sum(pool_scrap.map(if_prime, list(range(1000000))))
    pool_scrap = Pool(2)
    answer = sum(pool_scrap.map(if_prime, list(range(1000000))))

    print "Answer:", answer

    try:
        x = 6
        # print "Call if_prime(", x ,"): ", if_prime(x)
        # print "App complete."
    except:
        traceback.print_exc()
        # self.log.saveMessageToLog(a)
        print "Trigger Exception, traceback info forward to log file."
        traceback.print_exc(file=open("errlog.txt","a"))
        sys.exit(1) 

    print ""
    print "Main program ends"


