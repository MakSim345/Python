import os
import sys
import re
import os
import sys

"""
Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O)
who take turns marking the spaces in a 3x3 grid. The player who succeeds in placing
three respective marks in a horizontal, vertical, or diagonal rows (NW-SE and NE-SW)
wins the game.

But we will not be playing this game. You will be the referee for this games results. 
You are given a result of a game and you must determine if the game ends in a win or a 
draw as well as who will be the winner. Make sure to return "X" if the X-player wins 
and "O" if the O-player wins. If the game is a draw, return "D". 
"""

def checkio(_num_to_check):
    # print "number check:", _num_to_check
    first_win = False
    ret_val = "D"
    # a = ["X.O", "XX.", "XOO"]
    # a = ["O.O", "XXX", "XOO"]
    # a = ["O.O", "XOX", "XOO"]
    # a = [".O.","XXX",".O."]

    a = _num_to_check
    # print a
    FIRST =  a[0]
    SECOND = a[1]
    THIRD =  a[2]

    for i in range(3):
        # print i, "----------"
        if FIRST[i] == SECOND[i] == THIRD[i]:
            print i, ": ", FIRST[i], " - OK" 

            if (FIRST[i] != '.'):
                ret_val = FIRST[i]
                #if (not first_win):
                #    first_win = True
                #else:
                #    ret_val = "D"    
    #endfor    

    if FIRST[0] == FIRST[1] == FIRST[2]:
        print ": FIRST - OK"  
        if (FIRST[0] != '.'):
            ret_val = FIRST[0]

    if SECOND[0] == SECOND[1] == SECOND[2]:
        print ": SECOND - OK"
        if (SECOND[0] != '.'):
            ret_val = SECOND[0]

    if THIRD[0] == THIRD[1] == THIRD[2]:
        print ": THIRD - OK"    
        if (THIRD[0] != '.'):
            ret_val = THIRD[0]
            
    if FIRST[0] == SECOND[1] == THIRD[2]:
        print ": Left Cross - OK"    
        if (FIRST[0] != '.'):
            ret_val = FIRST[0]
            
    if FIRST[2] == SECOND[1] == THIRD[0]:
        print ": Right Cross - OK" 
        if (FIRST[2] != '.'):
            ret_val = FIRST[2]
            
    return ret_val

# main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    print "Main program start."
    print ""
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        ".O.",
        "XXX",
        ".O."]) == "X", "Xs wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    
    
    print ""    
    print "Main program end."