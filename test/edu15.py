#!/usr/bin/env python

#############################################################################
##
##
#############################################################################

import sys, os 
import traceback
import csv

def create_array():
    a = [676.7, 353, 433, 14, 14.565]
    # a.sort()
    # print a
    return a

def dictTest2(_dict):

    print "\nThe dictionary:"
    print _dict

    for _key in _dict:
            print _key, " - ", _dict[_key]
    #end_for
        
    print "\nSorted dictionary:"    
    for key in sorted(_dict.iterkeys()):
        print "%s: %s" % (key, (_dict[key]))
    #end_for    

    print sorted(_dict.iterkeys())

def sort_my_dict():
    author = {"php":"Rasmus Lerdorf",\
              "perl":"Larry Wall",\
              "tcl":"John Ousterhout",\
              "awk":"Brian Kernighan",\
              "java":"James Gosling",\
              "parrot":"Simon Cozens",\
              "python":"Guido van Rossum" }
    
    print author
    print "1--------------Sorted dict:"

    langs = author.keys()
    langs.sort()
    for language in langs:
        print language," - ",author[language]
    
    print "2--------------Sorted dict:"
    for key in sorted(author.iterkeys()):
        print "%s: %s" % (key, author[key])    

    for key in author.iteritems():
        print key
#end_def              

def dictTest():
    DeliveryStarted = 0
    DeliveryStopped = 1
    FGTotalFlowChanged = 2
    AgentTypeChanged = 3
    OxygenPercentageChanged = 4
    AirPercentageChanged = 5
    N2OPercentageChanged = 6
    AgentPercentageChanged = 7
    DummyAlarm = 8
    m_Array = {}  
    
    m_Array[DeliveryStarted]        = MyArray()
    m_Array[DeliveryStopped]        ="DeliveryStopped" 
    m_Array[FGTotalFlowChanged]     ="FGTotalFlowChanged" 
    m_Array[AgentTypeChanged]       ="AgentTypeChanged" 
    m_Array[OxygenPercentageChanged]="OxygenPercentageChanged" 
    m_Array[AirPercentageChanged]   ="AirPercentageChanged" 
    m_Array[N2OPercentageChanged]   ="N2OPercentageChanged" 
    m_Array[AgentPercentageChanged] ="AgentPercentageChanged" 
    m_Array[DummyAlarm]            ="DummyAlarm"
    
    if DeliveryStarted in m_Array:
        print "DeliveryStarted is in array"

    for key, value in m_Array.iteritems():
        print key, value    

    _current_status = m_Array[4] 
    print "DummyAlarm:", _current_status


def saveDict(file_name, dict_rap):
    file_dict = open(file_name, "wb")
    w = csv.writer(file_dict)

    for key, val in dict_rap.items():
        w.writerow([key, val])
    #end_for

    file_dict.close()
     
def readDict(file_name):
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



def dict_diff():
    
    fruit_avail = {'apples': 25, 'oranges': 0, 'mango': 12, 'pineapple': 0 }
    fruit_satch = {'apples': 1,  'oranges': 0, 'kiwi': 13 }

    available = set(fruit_avail.keys())
    satchel = set(fruit_satch.keys())
    # fruit not in your satchel, but that is available
    print available.difference(satchel)
    print satchel.difference(available)

def dropbox_test():
    
    dict_orig = {
    'D:/Dropbox/SOLO/this.log':   0xD959AC14,    
    'D:/Dropbox/SOLO/link.log':   0x94472987,    
    'D:/Dropbox/SOLO/award.log':  0x53FB3BEC,
    'D:/Dropbox/SOLO/ass.log':  0x53FB3BEE,
    'D:/Dropbox/SOLO/session.vim':0x6E5842CE
    }

    dict_next = {
    'D:/Dropbox/SOLO/this.log':   0xD945AC14,        
    'D:/Dropbox/SOLO/link.log':   0x94472907,    
    'D:/Dropbox/SOLO/award.log':  0x53FB3BEC,
    'D:/Dropbox/SOLO/crap.log':   0x456B3BEC,
    'D:/Dropbox/SOLO/session.vim':0x667842CE
    }

    #dictTest2(dict_orig)
    #dictTest2(dict_next)
    #dict_to_test = dict_next
    #dict_to_cmp = dict_orig
    compare_dict(dict_next, dict_orig, 'ADDED')
    compare_dict(dict_orig, dict_next, 'REMOVED')


def compare_dict(dict_to_test, dict_to_cmp, _rem = 'ADDED'):
    for _key in dict_to_test:
            # print _key, " - ", dict_to_test[_key]
            if _key in dict_to_cmp:
                # print "OK - key", _key, "exists in both dictionaries"
                # print dict_to_cmp[_key], dict_to_test[_key]                
                if dict_to_cmp[_key] == dict_to_test[_key]:
                    pass # print "file", _key, "was not changed"
                else:                    
                    print "CHANGED", ": <", _key, ">"
            else:
                print _rem, ": <", _key, ">"
    #end_for
    

if __name__ == "__main__":    

    print "Main program start."
    print ""

    try:
        #### Initially adding values ####
        _dict = {'a':23,'b':232,'c':13}
        
        for x in [1,2,3,4]: print (x ** 2)
        
    except NotImplementedError, e:
        print "1. Error occures:",  e
    except:
        print "2. Error occures: unknown"
        traceback.print_exc()    


    print "Main program ends"


