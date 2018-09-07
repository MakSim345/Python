#!/usr/bin/python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

# ============================================================
#
#
# ============================================================

import os
import urllib2
import time
import zlib
from list_files import list_files

# main entrance point:
if __name__ == "__main__":
    print u"Main app start."
    print ""
    
    search_path_main_box = u"d:/dev"
    # search_path_main_box = u"d:/TMP"
    # search_path_main_box = u"d:/Documents and Settings/aa027762/My Documents/[0] INBOX"
    _lst_fls = list_files(search_path_main_box)
    _lst_fls.run(True)
    
    print ""
    print "Main program end."
