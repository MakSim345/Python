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
import platform

# main entrance point:
if __name__ == "__main__":
    print "Python  has version:"
    print "1 - ", (sys.version)
    print "2 - ", (platform.python_version())
    print("The Python version is %s.%s.%s" % sys.version_info[:3])
    print "\nMain program end."
