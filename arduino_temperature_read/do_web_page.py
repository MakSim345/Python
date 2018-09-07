#!/usr/bin/python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

# ============================================================
# Description:
# ============================================================-

import sys, traceback
# from datetime import date, datetime, timedelta
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


class web_page_generator():
    def __init__(self, file_name_p = 'index.html'):
        ''' init class'''
        self.file_name = file_name_p
        self.set_connected(True)
        self.mth_str = month_str()
        self.set_temp_basement(12)
        self.set_temp_freezer(-21)
        self.set_uptime("0")

    def get_file_name(self):
        return self.file_name

    def set_connected(self, is_connected):
        ''' reflect connection to arduino'''
        self.connected = is_connected

    def get_month(self):
        '''return month in str'''
        return 1

    def run(self):
        '''return month in str'''
        # Open it in write mode:
        self.html_file = open(self.file_name, "w")

        # genertate static html page:
        self.do_page()

        # At the end, close the file again.
        self.html_file.close()

    def write_to_file(self, data_p = '\n'):
        self.html_file.write(data_p)
        # self.html_file.write('\n')

    def get_uptime(self):
        ''' return uptime value '''
        return self.uptime

    def set_uptime(self, new_uptime):
        ''' setup uptime value '''
        self.uptime = new_uptime

    def get_timestamp(self, _selector = "date"):

        _day = time.strftime("%d")
        _year = time.strftime("%Y")
        _month = time.strftime("%m")

        _date = _year + '-' +  self.mth_str.get_month(int(_month)) + '-' +  _day
        _time = time.strftime("%H:%M:%S")

        #print _date
        #print _time
        if _selector == "time":
             return _time
        else:
            return _date

    def set_temp_freezer(self, new_temp, min_temp=0, max_temp=0, avr_temp=0):
        '''set internal variable'''
        self.set_connected(True)
        self.freezer_temperature = str(new_temp)
        self.freezer_min_temperature = str(min_temp)
        self.freezer_max_temperature = str(max_temp)
        self.freezer_avr_temperature = "%.2f" % avr_temp

    def set_temp_basement(self, new_temp, min_temp=0, max_temp=0, avr_temp=0):
        '''set internal variable'''
        self.set_connected(True)
        self.basement_temperature = str(new_temp)
        self.basement_min_temperature = str(min_temp)
        self.basement_max_temperature = str(max_temp)
        self.basement_avr_temperature = "%.2f" % avr_temp

    def do_page(self):
        '''create complete static html page'''
        self.do_header()
        if (self.connected):
            self.do_data()
        else:
            self.do_no_connection()
        self.do_close_page()

    def do_header(self):
        '''make a header for html'''
        # =============Create an HTML page=================================================
        self.write_to_file("<!DOCTYPE HTML PUBLIC> ")
        self.write_to_file('<html lang="en">')
        self.write_to_file()
        self.write_to_file("<head> ")
        self.write_to_file()
        self.write_to_file("<meta http-equiv='Content-Type' content='text/html; charset=utf-8' /> ")
        self.write_to_file()
        self.write_to_file("<title> YS - Home temperature V0.1</title>")
        self.write_to_file()
        self.write_to_file("</head> ")
        self.write_to_file()

        '''Refresh the page every N seconds:'''
        self.write_to_file("<meta http-equiv='Refresh' content='60'>")
        self.write_to_file()

        self.write_to_file("<body>")
        # self.write_to_file("<hr />")#line =====================================
        self.write_to_file()
        self.write_to_file("<h1> Kuusimaenpolkku 5 </h1>")
        '''make a data sector'''
        self.write_to_file("<hr />") #line =====================================
        self.write_to_file("<h3> Time: ")
        self.write_to_file(self.get_timestamp("time"))
        self.write_to_file("  ")
        self.write_to_file(self.get_timestamp("data"))
        self.write_to_file("<h3> <font color = 'blue'> [Uptime: ")
        self.write_to_file(self.get_uptime())
        self.write_to_file("] </font>")
        self.write_to_file("<hr />") # line =====================================

    def do_data(self):
        self.write_to_file("<h2> Basement: ")
        self.write_to_file(self.basement_temperature)
        self.write_to_file(" &deg;C [")
        self.write_to_file(self.basement_min_temperature)
        self.write_to_file("...")
        self.write_to_file(self.basement_max_temperature)
        self.write_to_file("] Avr: ")
        self.write_to_file(self.basement_avr_temperature)
        self.write_to_file("<br> </h2>") #new line
        self.write_to_file("<h2> Freezer: ")
        self.write_to_file(self.freezer_temperature)
        self.write_to_file(" &deg;C [")
        self.write_to_file(self.freezer_min_temperature)
        self.write_to_file("...")
        self.write_to_file(self.freezer_max_temperature)
        self.write_to_file("] Avr: ")
        self.write_to_file(self.freezer_avr_temperature)
        self.write_to_file("<br> </h2> ")  #new line
        self.write_to_file("<hr />") #line =====================================

    def do_no_connection(self):
        self.write_to_file("</h3>") #new line
        self.write_to_file("<h3> <font color = 'red'> ERROR: No connection to sensors! </font>")
        self.write_to_file("<hr />") # line =====================================
        self.write_to_file("<h2> Basement: --.--")
        self.write_to_file(" &deg;C")
        self.write_to_file("<br> </h2>") #new line
        self.write_to_file("<h2> Freezer: --.--")
        self.write_to_file(" &deg;C")
        self.write_to_file("<br> </h2> ")  #new line
        self.write_to_file("<hr />") #line =====================================

    def do_close_page(self):
        ''' close html page'''
        self.write_to_file("</body></html>")

# main entrance point:
if __name__ == "__main__":

    print "Main program begins"
    print ""

    a = web_page_generator()
    a.set_temp_basement("12")
    a.set_temp_freezer("-18")
    a.set_connected(True)
    a.run()
    # print a.get_timestamp()

    print ""
    print "Main program ends"



