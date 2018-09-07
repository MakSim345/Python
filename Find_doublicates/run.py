#!/usr/bin/python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

# ============================================================
#
#
# ============================================================
#
# ============================================================
# ============================================================

import os
import urllib2
import time
import zlib
from search_and_destroy import *
from search_dublicates import search_dublicates
from file_manager import md5_hash
from file_manager import file_manager

class logEngine(): 
    
    def __init__(self):
        self._log_file_name = 'dublicate_search.log'

    def saveToLog(self, _text):        
        file = open(self._log_file_name, "a")
        file.write(time.strftime("%Y-%m-%d %H:%M:%S\n"))
        file.write("TRACE:\n")
        file.write(_text)
        file.write("\n-------------------------------------\n")
        file.close()

def open_file_safe(_file_name):
    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except IOError as (errno, strerror):
        print "\nI/O error({0}): {1}".format(errno, strerror)
    except ValueError:
        print "\nCould not convert data to an integer."
    except:
        print "\nUnexpected error:", sys.exc_info()[0]
        raise
    
# main entrance point:
if __name__ == "__main__":
    # print u"Программа началась."
    print ""
    
    # search_path_main_box = "D:/Documents and Settings/aa027762/My Documents/[1] Inbox"
    # search_path_main_box = "D:/Documents and Settings/aa027762/My Documents/[2] To read"
    # search_path_main_box = "D:/Documents and Settings/aa027762/My Documents/[3] GE Docs/Tech Manuals"    
    # search_path_main_box = "D:/Documents and Settings/aa027762/My Documents/SW Books 2002"
    # search_path_main_box = "D:/Documents and Settings/aa027762/My Documents"
    # search_path_main_box = "H:/NoteBook_bkp/[2] video/RUS MyLbTbI"
    #search_path_main_box = "H:/NoteBook_bkp/NOKIA-BKP/urpbI"
    #search_path_main_box = "h:/[3] audio/music"
    #search_path_main_box = "e:/[4] Music"
    #search_path_main_box = "d:/Documents and Settings/aa027762/My Documents/My Pictures/2007/2007-02 (haat-3)"
    #search_path_main_box = "C:/"
    # search_path_main_box = "E:/tmp"
    # search_path_main_box = "d:/Documents and Settings/aa027762/My Documents/My Pictures/Muxacuk"
    #search_path_main_box = "d:/Documents and Settings/aa027762/My Documents/[3] GE Docs"

    # search_path_main_box = "f:/[5] pictures/2010/foto/video"
    # search_path_main_box = "d:/Dropbox/[4] video/"
    # search_path_main_box = "d:/Dropbox/photos/"
    # search_path_main_box = "D:/Dropbox/[1] Books/SW Books"
    # search_path_main_box = "D:/Dropbox/Photos/Camera Uploads Nadia/Nokia"
    # search_path_main_box = "D:/tmp"
    # search_path_main_box = "e:/Dropbox/Photos/MUSEUM/To_Phone"    
    # search_path_main_box = "e:/[1] Audio/[1] Audiobooks/Suomi Kieli"
    #search_path_main_box = "C:/[2] dev/Genie_main_trunk"
    # search_path_main_box = "E:/Dropbox/[1] Books"
    #search_path_main_box = "C:/Dropbox/[7] Utils"
    # search_path_main_box = "C:/[0] INBOX"
    search_path_main_box = "D:/Dropbox/Photos/2013"
    # search_path_main_box = "C:/Dropbox/Photos/Camera Uploads Nadia/Nokia"
    #search_path_main_box = "C:/SkyDrive/[5] PHOTO"
    #search_path_main_box = "C:/Dropbox"
    #search_path_main_box = "C:/SkyDrive/[6] pictures"
    #search_path_main_box = "D:/Documents and Settings/aa027762/My Documents/[0] INBOX/Microcontrollers"

    
    _sd = search_dublicates(search_path_main_box)
    NO_ERASE_FILES = False
    ERASE_FILES = True
    _sd.run(ERASE_FILES)

    print ""
    print "Main program end."
