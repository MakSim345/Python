#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# ============================================================
#
# APR-2015.
# YS. 
# Script for create a string with current date minus 30 days 
# for RegWeb
# The result string shall be in the Clipboard, use Ctrl+V.
# ============================================================

import string
import sys
import time
import win32clipboard
from datetime import datetime, timedelta


def test_date():
    'Получить текущее время и дату'
    print datetime.now()
    #> 2010-08-14 02:58:15.057495
    
    d = datetime.today()
    print d
    #> 2010-08-14 02:58:15.057538

    'Форматированный вывод'
    print d.strftime('%y-%m-%d %H:%M:%S')
    #> 10-08-14 02:58:15

    'Сдвинуть время'
    print d + timedelta(days=1, hours=1)
    #> 2010-08-15 03:58:15.057538

    'Конвертировать время POSIX в datetime'
    print datetime.fromtimestamp(time.time())
    #> 2010-08-14 02:58:15.057613

    'Изменить атрибут'
    print d.replace(year=2011,hour=11)
    #> 2011-08-14 11:58:15.057538
    #replace(year, month, day, hour, minute, second, microsecond, tzinfo)

    'Получить кортеж'
    print d.timetuple()
    #> time.struct_time(tm_year=2010, tm_mon=8, tm_mday=14, tm_hour=2,
    #> tm_min=58, tm_sec=15, tm_wday=5, tm_yday=226, tm_isdst=-1)

    'Получиь день недели, 0 - Пн, 6 - Вс'
    print d.weekday()
    #> 5

    'Получить дату'
    print d.date()
    #> 2010-08-14

    'Получить время'
    print d.timetz()
    #> 02:58:15.057538

    'Сложить дату и время'
    print d.combine(d.date(),d.timetz())
    #> 2010-08-14 02:58:15.057538

def copy(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()

if __name__ == "__main__":
    #print 'Number of arguments:', len(sys.argv), 'arguments.'
    #print 'Argument List:', str(sys.argv)
    d = datetime.today()
    print d

    #shift date:
    dd = d + timedelta(days=-30)
    print dd
    
    start_date = dd.strftime('%d.%m.%y')
    end_date = d.strftime('%d.%m.%y')
    s = "http://regweb.euro.med.ge.com/report.asp?tid=1&sdate={}&edate={}&sb-show=Show"
    #print s
    s = s.format(start_date, end_date)
    print s
    copy(s)
    print "Now paste and observe"
    


