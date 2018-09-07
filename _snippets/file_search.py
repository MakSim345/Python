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
import sys

replacement = "newString"
toReplace = "oldString"
rootdir = "pathToProject"
_all_files_ctr = 0


#!/usr/bin/python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-
# ============================================================
#
# Author:         YS
#
# ============================================================
# 
# ============================================================
import os, string
import subprocess
import glob
import shutil
import time

class month_str():
    def __init__(self):
        ''' init class'''
        STR_JAN="JAN"
        STR_FEB="FEB"
        STR_MAR="MAR"
        STR_APR="APR"
        STR_MAY="MAY"
        STR_JUN="JUN"
        STR_JUL="JUL"
        STR_AUG="AUG"
        STR_SEP="SEP"
        STR_OCT="OCT"
        STR_NOV="NOV"
        STR_DEC="DEC"
        self._month_str = {1:STR_JAN, 2:STR_FEB, 3:STR_MAR, 4:STR_APR,
                           5:STR_MAY, 6:STR_JUN, 7:STR_JUL, 8:STR_AUG,
                           9:STR_SEP, 10:STR_OCT, 11:STR_NOV, 12:STR_DEC}
    
    def get_month(self, month_int):
        '''return month in str'''
        return self._month_str.get(int(month_int))


class logEngine():
    def __init__(self):
        self.setLogFileName('results.log')
        self.mth_str = month_str()

    def setLogFileName(self, _file_name):
        self._log_file_name = _file_name
    
    def get_cur_date(self):
        '''return date and time'''
        _day = time.strftime("%d")
        _year = time.strftime("%Y")
        _month = time.strftime("%m")        
        _date = _day + '-' + self.mth_str.get_month(int(_month)) + '-' + _year        
        _ret_val = _date + ' ' + time.strftime("%H:%M:%S")
        return _ret_val
        
    def saveToLog(self, _text):
        file = open(self._log_file_name, "a")
        # file.write(time.strftime("%Y-%m-%d %H:%M:%S\n"))        
        _start_time = self.get_cur_date()
        file.write(_start_time)
        file.write(_text)
        file.write("\n-------------------------------------\n")
        file.close()


def search_for_files_cur_dir(file_extend):
    selected_files = []
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for file in files:
        # do something
        # filePath = rootdir + '/' + file
        # print "file - ", file, 'ext: ' + file[-4:]
        ext = os.path.splitext(file)# [1]
        print file, ext
        # ext = string.split(file, '.')
        # print file, ext[1]
        if ext[1] in file_extend:
                print "add file ", file
                selected_files.append(file)
    
    if not selected_files:
        print "no files to extract"        
    else:
        print "Result:"
        print selected_files
    
    return selected_files
    

def search_for_files(rootdir, file_extend):
    """
    make a list of files with given extention in given folder
    """
    selected_files = []
    for root, sub_folders, files in os.walk(rootdir):
        for item_file in files:
            file_path = os.path.join(root, item_file)
            ext = string.split(item_file, '.')
            if ext[1] in file_extend:
                selected_files.append(file_path)
            
    print "Result:"
    print selected_files # filePath
    return selected_files

def copy_and_remove(file_list_array, destination_path):
    log_eng = logEngine()
    str_result = ''
    if not file_list_array:
        return

    for each in file_list_array:
        print each
        str_result = str_result + '\n' + str(each)
        shutil.copy(each, destination_path)
        os.remove (each)

    log_eng.saveToLog(str_result)

def openFolder(path):
    subprocess.check_call(['explorer', path])

# main entrance point:
if __name__ == "__main__":    
    #print "Main program start."
    #print ""
    
    # search_path_main_box = "D:/dev/Python/unpack"
    search_path_main_box = os.getcwd()
    
    # dest_path = "C:/video_tmp" # does not work with openFolder().
    dest_path = "C:\\video_tmp"
    
    file_extender = ['.jpg', '.pdf', '.mkv', '.mp4', '.avi', '.srt', '.fb2', '.mov', '.MOV']

    # result_array = search_for_files(search_path_main_box, file_extender)
    result_array = search_for_files_cur_dir(file_extender)
    copy_and_remove(result_array, dest_path)
    
    openFolder(dest_path)

    #print ""    
    #print "Main program end."


def run_action(_filename):
    _is_sms = False # reset sms flag

    if not os.path.exists(_filename):
        sys.stderr.write("Info: '"+self.filename+"' does not exist. Nothing to do\n")
        # sys.exit(1)
    else:
        # _action()
        sys.stderr.write("Info: '"+self.filename+"' does exist.\n")
    # endif 
    return _is_sms


_dict = {"0":"0"}
# main entrance point:
if __name__ == "__main__":
    print ""
    rootdir = os.getcwd()
    for root, subFolders, files in os.walk(rootdir):
        ''' walk through all files in folder'''
        if '.svn' in subFolders:
            subFolders.remove('.svn')
        #endif

        for name in files:
            _file_name = os.path.join(path, name)
            _all_files_ctr = _all_files_ctr + 1
            # self._file_hash  = md5.get_md5sum(self._file_name)

            print "File:  " + _file_name
            _dict[_all_files_ctr] = _file_name # add item to dictionary, filename as key
        #end_for
    #end_for

        #for _key in self._dict:
        #    print _key, " - ", self._dict[_key]
        # print self._dict
        #for key in sorted(self._dict.iterkeys()):
        #    print "%s: %s" % (key, (self._dict[key]))

        # print sorted(self._dict.iterkeys())
    
    print "Main program end."
