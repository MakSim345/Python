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

# main entrance point:
if __name__ == "__main__":
    print ""

    a = "545.2222"
    print float(a)
    # 545.22220000000004
    print int(float(a))
    #545
    b = '10AFCC'
    new_b = '0x' + b
    print int(new_b, 16)
    # 1093580
    hex(1093580)
    #'0x10afcc'    
    
    print "Main program end."
