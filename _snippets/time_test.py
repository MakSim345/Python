from urllib import urlopen
import os

proxies = {'http': 'http://3.187.4.17:88'}
#Request google index page
headers = urlopen('http://google.com/', proxies=proxies).info()
s = urlopen('http://google.com/', proxies=proxies).read()
date = "date -s \"" + headers.getheader('Date') + "\""

print s

print "Google Date:" + date
    
