import os
import sys
import re

"""

"""
def check_pawn_around(_curr, _set_of_pawn):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    ret_val = 0
    print "check - ", _curr
    cur_let =  _curr[:1]
    cur_num =  _curr[1:]
    #print  "Position: \nletter:", cur_let, " number:", cur_num
    # calc save sets:
    
    safe_num = int(cur_num) - 1
    if safe_num <= 0:
        print "safe number not EXIST"
        return False
    else:
        print "safe number:", str(safe_num)
    #endif    
    
    _t1 = letters.index(cur_let) + 1
    if (_t1 >= len(letters)): # do not go out of range
        print "safe letter 1 not EXIST"
    else:
        safe1 = letters[_t1] + str(safe_num)
        print "safe1:", safe1
        if (safe1 in _set_of_pawn):
           print "We have one safe!"
           return True
        #endif
    #endif    
            
    _t1 = letters.index(cur_let) - 1    
    if (_t1 < 0):
        print "safe letter 2 not EXIST"        
    else:
        safe2 = letters[_t1] + str(safe_num)
        print "safe2:", safe2
        if (safe2 in _set_of_pawn):
            print "We have one safe!"
            return True
        #endif       
    #endif   

    return False # default return if no success

def safe_pawns(_num_to_check):
    # print "number check:", _num_to_check
    ret_val = 0
    
    print _num_to_check

    for i in _num_to_check:
        print ""
        if (check_pawn_around(i, _num_to_check)):
            ret_val += 1
    
    return ret_val

def check_connection2(network, first, second):
    print network
    net_1 = []
    net_2 = []
    a = re.split('-', network[0])
    net_1_flag = False    
    net_2_flag = False    
    net_1.append (a[0])
    net_1.append (a[1])
       
    for i in network[0:]:
        net_1_flag = False
        a = re.split('-', i)
        print a
        _tmp1 = a[0]
        _tmp2 = a[1]
        if _tmp1 in net_1:
            net_1_flag = True
            if _tmp2 not in net_1:
                net_1.append(_tmp2)
            #endif
        #endif
        if _tmp2 in net_1:
            net_1_flag = True            
            if _tmp1 not in net_1:
                net_1.append(_tmp1)
            #endif    
        #endif
        if (not net_1_flag):
            if (not net_2_flag):
                net_2_flag = True
                net_2.append (_tmp1)
                net_2.append (_tmp2)
            else:    
                if _tmp1 in net_2:            
                    if _tmp2 not in net_2:
                        net_2.append(_tmp2)
                    #endif
                #endif    
                if _tmp2 in net_2:            
                    if _tmp1 not in net_2:
                        net_2.append(_tmp1)
                    #endif   
                #endif       
            #endif   
        #endif
        print "net_1: ", net_1
        print "net_2: ", net_2                
    #end for        
    print "net_1: ", net_1
    print "net_2: ", net_2

    ret_val = False
    print "Main test:", first, second
    if ((first in net_1) and (second in net_1)): ret_val = True
    if ((first in net_2) and (second in net_2)): ret_val = True
    
    return ret_val

def check_connection(network, first, second):
    print network
    net_1 = []
    net_2 = []
    a = re.split('-', network[0])
    net_1_flag = True
    net_2_flag = False    
    net_1.append (a[0])
    net_1.append (a[1])
    
    while net_1_flag:
        net_1_flag = False
        for i in network[0:]:
            a = re.split('-', i)
            # print a
            _tmp1 = a[0]
            _tmp2 = a[1]
            if _tmp1 in net_1:                
                if _tmp2 not in net_1:
                    net_1.append(_tmp2)
                    net_1_flag = True
                #endif
            #endif
            if _tmp2 in net_1:                
                if _tmp1 not in net_1:
                    net_1.append(_tmp1)
                    net_1_flag = True 
                #endif    
            #endif
        #end for        
    #end while

    for i in network:
        # print i
        a = re.split('-', i)
        # print a
        _tmp1 = a[0]
        _tmp2 = a[1]
        if ((_tmp1 in net_1) or (_tmp2 in net_1)):
            pass
        else:
            net_2.append(_tmp1)
            net_2.append(_tmp2)    

    print "-net_1: ", net_1
    print "-net_2: ", net_2

    ret_val = False
    print "Main test:", first, second
    if ((first in net_1) and (second in net_1)): ret_val = True
    if ((first in net_2) and (second in net_2)): ret_val = True
    
    return ret_val


# main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    print "Main program start."
    print ""
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."    
    assert check_connection(
        ("nikola-robin","batman-nwing","mr99-batman","mr99-robin",
         "dr101-out00","out00-nwing",),"dr101","mr99") == True, "Super Scout"
    
    print "Main program end."

