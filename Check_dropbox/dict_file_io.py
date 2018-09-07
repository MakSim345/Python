#!/usr/bin/python
# ============================================================
#
#
# ============================================================
#
# Author:  YS
# Data:    FEB-2014
#
# ============================================================
# Description: file read/write wrapper for dictionary.
# ============================================================
import os
import csv
 
def saveDict(file_name, dict_rap):
    file_dict = open(file_name, "wb")
    w = csv.writer(file_dict)

    for key, val in dict_rap.items():
        w.writerow([key, val])
    #end_for

    file_dict.close()
     
def readDict(file_name):
    #check if file exists:
    if not os.path.exists(file_name):
        print "ERROR: File " + file_name + " does not exists!"
        return

    file_dict = open(file_name,'rb')    
    dict_rap = {}
     
    for key, val in csv.reader(file_dict):
        res = '0x'+str(val)
        # print res
        val =  hex(int(res, 16))
        # print key, val
        dict_rap[key] = eval(val)
    #end_for    
    file_dict.close()
    return(dict_rap)

def saveMessageToLog(messageBody):
    _log_file_name = "result.log"
    file = open(_log_file_name, "a")
    file.write(time.strftime("%Y-%m-%d %H:%M:%S\n"))
    file.write(messageBody + "\n")
    file.close()

def compare_dict(dict_to_test, dict_to_cmp, _rem = 'ADDED'):
    ret_val = ''
    tmp_str = ''
    for _key in dict_to_test:
        if _key in dict_to_cmp:
            if _rem == 'CHANGED':
                if dict_to_cmp[_key] == dict_to_test[_key]:
                    pass # print "file", _key, "was not changed"
                else:
                    tmp_str = _rem + ": <" + _key + ">"
                    ret_val = ret_val + '\n' + tmp_str
                #endif
            #endif    
        #endif
        else:
            if _rem == 'CHANGED':
                pass
            else:    
                tmp_str = _rem + ": <" + _key + ">"
                ret_val = ret_val + '\n' + tmp_str
        #endif    
    #end_for
    return ret_val


def compare_dict_bkp(dict_to_test, dict_to_cmp, _rem = 'ADDED'):
    for _key in dict_to_test:
        if _key in dict_to_cmp:
            if _rem == 'CHANGED':
                if dict_to_cmp[_key] == dict_to_test[_key]:
                    pass # print "file", _key, "was not changed"
                else:               
                    ret_val = _rem, dict_to_cmp[_key], ": <", _key, ">"
                    print _rem, dict_to_cmp[_key], ": <", _key, ">"                    
                #endif
            #endif    
        #endif
        else:
            if _rem == 'CHANGED':
                pass
            else:    
                print _rem, ": <", _key, ">"
        #endif    
    #end_for
#end_def
