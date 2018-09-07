import os
import sys

"""
A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall.
With this strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit
on that square. We have several white pawns on the chess board and only white pawns. 
You should design your code to find how many pawns are safe. 
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

# main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    print "Main program start."
    print ""
    
    # print safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})
    # print safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})
    # print safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})
    # print safe_pawns({"a1","b2","c3","d4","e5","f6","g7","h8"})
    safe_pawns({"b2"})
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    #assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    
    print ""    
    print "Main program end."
