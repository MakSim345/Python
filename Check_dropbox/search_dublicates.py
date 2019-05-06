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
# Description: .
# ============================================================

import os
import sys
import urllib2
import time
import zlib
from search_and_destroy import *
from file_manager import md5_hash
from file_manager import file_manager
from log_engine import *
from dict_file_io import *

def open_file_safe(_file_name_to_open):
    try:
        f = open(_file_name_to_open)
        s = f.readline()
        i = int(s.strip())
    except IOError as (errno, strerror):
        print "\nI/O error({0}): {1}".format(errno, strerror)
    except ValueError:
        print "\nCould not convert data to an integer."
    except:
        print "\nUnexpected error:", sys.exc_info()[0]
        raise


class search_dublicates():
    name = "search_dublicates"

    def __init__(self, arg=''):
        self.authority = 0
        self.set_path(arg)
        self._counter = 0
        self._all_files_ctr = 0
        self.__hash = 0
        self._ret_val_error = "ERR"
        self._trace = logEngine()
        self._fm = file_manager()
        self._dict = {"0":"0"}
        self._file_hash = 0
        self._database_file = "new_dropbox_db.csv"
        self._database_old_file = "old_dropbox_db.csv"

    def set_path(self, _path):
        self._search_path = _path
        if os.path.exists(self._search_path):
            self.authority = 1
        else:
            print "Error: Path " + self._search_path + " is invalid!"
    #end def

    def digest(self):
        return self.__hash & 0xffffffff

    def hexdigest(self):
        return '%08x' % (self.digest())

    def update(self, arg):
        self.__hash = zlib.crc32(arg, self.__hash)

    def internal_log (self):
        self._counter = self._counter + 1
        _str_to_log =  "- ATTN:(" + self._file_hash + " - " + str(self._file_size) + ") Found dublicate for follow files: \n" + self._file_name + "\n" + self._dict[self._file_hash]
        print ""
        print _str_to_log
        self._trace.saveToLog(_str_to_log)
        _str_to_log = "Same files counter = " + str(self._counter)
        print _str_to_log
        print ""
        self._trace.saveToLog(_str_to_log)

    def run(self, _erase_dub = False):
        ''' main loop for app'''
        if not self.authority:
            _str_to_log = "Error: Path " + self._search_path + " is invalid!"
            self._trace.saveToLog(_str_to_log)
            return

        # rename old database file to give place for next one:
        self._fm.rename_file(self._database_file, self._database_old_file)
        # Erase old database file to give place for next one:
        # self._fm.remove_file(self._database_file)
        
        _str_ignore_dir = '.dropbox.cache'    
        for path, subdirs, files in os.walk(self._search_path):
            if _str_ignore_dir in subdirs:
                print _str_ignore_dir + " - ignored"
                subdirs.remove(_str_ignore_dir)
            for name in files:
                self._file_name = os.path.join(path, name)
                self._all_files_ctr = self._all_files_ctr + 1
                # self._file_hash  = md5.get_md5sum(self._file_name)

                print "File:  " + self._file_name
                self._file_hash  = self.crc_file(self._file_name)
                print "CRC32: " + self._file_hash

                if self._file_hash in self._dict:
                    # self.internal_log()
                    if _erase_dub:
                        self._fm.remove_file(self._file_name) # delete file from disk, by file_manager API.
                    #endif
                else:
                    if (self._file_hash == self._ret_val_error):
                        print "File omitted\n"
                    else:
                        # self._dict[self._file_hash] = self._file_name # add item to dictionary
                        self._dict[self._file_name] = self._file_hash # add item to dictionary, filename as key
                    #endif
                #end_else    
            #end_for
        #end_for

        #for _key in self._dict:
        #    print _key, " - ", self._dict[_key]
        # print self._dict
        #for key in sorted(self._dict.iterkeys()):
        #    print "%s: %s" % (key, (self._dict[key]))

        # print sorted(self._dict.iterkeys())

        _str_to_log = "Total number of checked files: " + str(self._all_files_ctr)
        print _str_to_log
        #self._trace.saveToLog(_str_to_log)
        # _str_to_log = "Same files counter = " + str(self._counter)
        # print _str_to_log
        print ""
        self._trace.saveToLog(_str_to_log)
        
        saveDict(self._database_file, self._dict)

    def compare_dictionaryes(self):
        '''ATTN: this function shall call by an object! Outside of class'''
        dict_orig = readDict(self._database_old_file)
        dict_next = readDict(self._database_file)
        
        a = compare_dict(dict_next, dict_orig, 'ADDED')
        b = compare_dict(dict_orig, dict_next, 'REMOVED')
        c = compare_dict(dict_orig, dict_next, 'CHANGED')

        # print "Result:", a, b, c
        # put results to a list and sort them:
        messageBody = a.split('\n') + b.split('\n')  + c.split('\n')
        messageBody.sort()

        #convert list to a string:
        retMessageBody = '\n'.join(messageBody)
        print retMessageBody
            
        self._trace.saveToLog(retMessageBody)

        #make a backup for today:
        timestr = time.strftime("%Y-%m-%d")
        _str_file_name_to_bkp = timestr+'.csv'
        self._fm.remove_file(_str_file_name_to_bkp)
        self._fm.rename_file(self._database_old_file, _str_file_name_to_bkp)

        retMessageBody = timestr + "\n" + retMessageBody
        return retMessageBody # for sending via e-mail
        
    def crc_file(self, _file_name_to_open):
        prev = 0
        try:
            _file = open(_file_name_to_open, "rb")
            self._file_size = os.path.getsize(self._file_name)
        except IOError as (errno, strerror):
            print "\nI/O error({0}): {1}".format(errno, strerror)
            return self._ret_val_error
        except ValueError:
            print "\nCould not convert data to an integer."
            return self._ret_val_error
        except:
            print "\nUnexpected error:", sys.exc_info()[0]
            return self._ret_val_error
            raise

        #for eachLine in _file:
        #    prev = zlib.crc32(eachLine, prev)
        #return "%X"%(prev & 0xFFFFFFFF)
        try:
            for eachLine in self.read_in_chunks(_file):
                prev = zlib.crc32(eachLine, prev)
        except:
            _str_to_log = "Error in crc_file(): " + _file_name_to_open + " can not be read!"
            self._trace.saveToLog(_str_to_log)
            #self._trace.saveToLog(sys.exc_info()[0])
            print "\nUnexpected error:", sys.exc_info()[0]
            return "%X"%(prev & 0xFFFFFFFF)
            raise

        return "%X"%(prev & 0xFFFFFFFF)

    def read_in_chunks(self, file_object, chunk_size=1024):
        """Lazy function (generator) to read a file piece by piece.
        Default chunk size: 1k."""
        file_size_dl = 0
        while True:
            data = file_object.read(chunk_size)
            #---------------------------------------
            #file_size_dl += len(data)
            #status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / self._file_size)
            #status = status + chr(8)*(len(status)+1)
            #print status,
            #----------------------------------------
            if not data:
                break
            yield data
