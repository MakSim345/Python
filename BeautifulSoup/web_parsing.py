#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib2
import sys, traceback

import csv
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

def checkConnection(): 
    '''Check an  internet connection'''
    try:
        response = urllib2.urlopen('http://google.com', timeout = 1)
        return True
    except urllib2.URLError as err: pass
    return False

def make_all(urlP):
    hml = get_html(urlP)
    data = get_page_data(html)
    write_cvs (data)

def get_all_links(html, linksP):
    # 1. clean file without delete:
    f = open('coin.cvs', 'w')
    f.close()

    #2. work with html code
    soup = BeautifulSoup(html, 'lxml')
    # print soup
    href = soup.find_all('div', class_ = 'wm_countries')
    # print href 
    for i in href:
        for link in i.find_all ('a'):
            linksP += [link['href']]
    # print linksP

    return linksP
            
def get_html(urlP):
    retVal = requests.get(urlP)
    return retVal.text

def run_scrapper():
    # print "main here - !"
    url = 'http://banknotes.finance.ua'
    links = []
    # get all links from the website inti 
    all_links = get_all_links (get_html(url), links)

    # multithreading:
    with Pool(2) as pool_scrap:
        pool_scrap.map (make_all, all_links)
    #end_with
        
# main entrance point:
if __name__ == "__main__":

    print "Main program begins"
    print ""
    
    if (checkConnection()):
        run_scrapper()
    else:
        print "No INTERNET connection available. Check your PROXY."

    print ""
    print "Main program ends"
