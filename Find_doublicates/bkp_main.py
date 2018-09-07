#!/usr/bin/python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

# ============================================================
#
#
# ============================================================
#
#
# Author:         YS 
#
# ============================================================
# ============================================================

import os
import urllib2
import time
import zlib
from search_and_destroy import *
from file_manager import md5_hash
from file_manager import file_manager

def search_for_files(rootdir, file_extend):
    selected_files = []
    for root, subFolders, files in os.walk(rootdir):
        for file in files:

            filePath = rootdir + '/' + file
            ext = string.split(file, '.')
            if file_extend in ext:
                print "add file ", filePath
                selected_files.append(filePath)
            #endif
        #end for
    #end for

    # print selected_files# filePath
    return selected_files

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

def crc_file(_file_name):
    prev = 0
    _ret_val_error = "ERR"
    try:
        _file = open(_file_name,"rb")        
    except IOError as (errno, strerror):
        print "\nI/O error({0}): {1}".format(errno, strerror)
        return _ret_val_error
    except ValueError:
        print "\nCould not convert data to an integer."
        return _ret_val_error
    except:
        print "\nUnexpected error:", sys.exc_info()[0]
        return _ret_val_error
        raise

    for eachLine in _file:
        prev = zlib.crc32(eachLine, prev)
    return "%X"%(prev & 0xFFFFFFFF)

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
    print u"Программа началась."
    print ""
    _ret_val_error = "ERR"
    _trace = logEngine()
    _fm = file_manager()
    _dict = {"0":"0"}
    md5 = md5_hash()
    _counter = 0
    _all_files_ctr = 0
    # search_path_main_box = "D:/Documents and Settings/aa027762/My Documents/[1] Inbox"
    # search_path_main_box = "D:/Documents and Settings/aa027762/My Documents/[2] To read"
    # search_path_main_box = "D:/Documents and Settings/aa027762/My Documents/SW Books 2002"
    search_path_main_box = "H:/NoteBook_bkp/NOKIA-BKP"
    #search_path_main_box = "D:/Documents and Settings/aa027762/My Documents"
    # search_path_main_box = "H:/"
    
    # result_array = search_for_torrent(search_path_main_box, torren_file_extender)
    for path, subdirs, files in os.walk(search_path_main_box):
        for name in files:
            _file_name = os.path.join(path, name)
            _all_files_ctr = _all_files_ctr + 1
            # _md5_hash  = md5.get_md5sum(_file_name)
            _md5_hash  = crc_file(_file_name)
            
            # _file_name = _file_name.decode('cp1252').encode('utf8')
            # _file_name = _file_name.decode('utf8')
            #_file_name = _file_name.decode('cp1252')
            
            print "File:  " + _file_name
            print "CRC32: " + _md5_hash

            if _md5_hash in _dict:
                _counter = _counter + 1
                _str_to_log =  "- ATTN:(" + _md5_hash + ") Found dublicate for follow files: \n" + _file_name + "\n" + _dict[_md5_hash]
                print ""
                print _str_to_log                
                _trace.saveToLog(_str_to_log)

                _str_to_log = "Same files counter = " + str(_counter)
                
                print _str_to_log
                print ""
                _trace.saveToLog(_str_to_log)
                # _fm.remove_file(_file_name)

            else:
                if (_md5_hash == _ret_val_error):
                    print "File omitted\n"
                else:   
                    _dict[_md5_hash] = _file_name # add item to dictionary
                
    # copy_and_remove(result_array, dest_path)
    # print _dict
    
    _str_to_log = "Total number of checked files: " + str(_all_files_ctr)
    print _str_to_log
    _trace.saveToLog(_str_to_log)

    print ""
    print "Main program end."
