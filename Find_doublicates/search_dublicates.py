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

import os, sys
import urllib2
import time
import zlib
import hashlib
import subprocess
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
        self.setLogFileName('dublicates.log')

    def setLogFileName(self, _file_name):
        self._log_file_name = _file_name

    def saveToLog(self, _text):
        file = open(self._log_file_name, "a")
        file.write(time.strftime("%Y-%m-%d %H:%M:%S\n"))
        file.write("TRACE:\n")
        file.write(_text)
        file.write("\n-------------------------------------\n")
        file.close()

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
        if not self.authority:
            _str_to_log = "Error: Path " + self._search_path + " is invalid!"
            self._trace.saveToLog(_str_to_log)
            return

        for path, subdirs, files in os.walk(self._search_path):
            for name in files:
                self._file_name = os.path.join(path, name)
                self._all_files_ctr = self._all_files_ctr + 1
                # self._file_hash  = md5.get_md5sum(self._file_name)

                print "File:  " + self._file_name
                self._file_hash  = self.crc_file(self._file_name)
                print "CRC32: " + self._file_hash

                if self._file_hash in self._dict:
                    self.internal_log()
                    if _erase_dub:
                        self._fm.remove_file(self._file_name)
                    #endif
                else:
                    if (self._file_hash == self._ret_val_error):
                        print "File omitted\n"
                    else:
                        self._dict[self._file_hash] = self._file_name # add item to dictionary

        #for _key in self._dict:
        #    print _key, " - ", self._dict[_key]
        # print self._dict
        #for key in sorted(self._dict.iterkeys()):
        #    print "%s: %s" % (key, (self._dict[key]))

        # print sorted(self._dict.iterkeys())

        _str_to_log = "Total number of checked files: " + str(self._all_files_ctr)
        print _str_to_log
        self._trace.saveToLog(_str_to_log)
        _str_to_log = "Same files counter = " + str(self._counter)
        print _str_to_log
        print ""
        self._trace.saveToLog(_str_to_log)

    def crc_file_md5(self, _filename):
        prev = 0
        resultMD5 = []
        self._file_size = os.path.getsize(_filename)
        try:
            cmd = ['md5sum', _filename]
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            resultMD5.append(proc.stdout.readline())
            proc.stdout.close()
            # print "calc_md5_exe: ", resultMD5[0]
            return resultMD5[0][1:33]
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
    #endif

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

        for eachLine in self.read_in_chunks(_file):
            prev = zlib.crc32(eachLine, prev)
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
