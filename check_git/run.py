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
from check_git import *

# main entrance point:
if __name__ == "__main__":
    # print u"Программа началась."
    print ""

    search_path_main_box = "D:/dev/"
    # search_path_main_box = "D:/dev/git_test"
    
    dir_list = search_for_files(search_path_main_box)
    print "Folder .git exist in follow:"
    for dir_name in dir_list:
        print '\n-----------------------------'
        print dir_name
        os.chdir(dir_name)
        os.system('git status')
    

    print ""
    print "Main program end."
