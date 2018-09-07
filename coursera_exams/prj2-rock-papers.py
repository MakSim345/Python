#!/usr/bin/env python

#############################################################################
##
## Coursera SEP-2014. Exam 2
##
## The rock-paper-scissors-lizard-Spock 
##
#############################################################################

import math
import sys, os
import random 

# Rock-paper-scissors-lizard-Spock app

import random 

def name_to_number(name):
    '''convert given name to a number'''    
    if (name == "rock"):
        retVal = 0
    elif (name == "Spock"):
        retVal = 1
    elif (name == "paper"):
        retVal = 2    
    elif (name == "lizard"):
        retVal = 3
    elif (name == "scissors"):
        retVal = 4     
    else:
        retVal = -100
    #endif    
    return retVal    

def number_to_name(number):
    '''convert given number to a name '''    
    if (number == 0):
        retVal = "rock"
    elif (number == 1):
        retVal = "Spock"
    elif (number == 2):
        retVal = "paper" 
    elif (number == 3):
        retVal = "lizard"
    elif (number == 4):
        retVal = "scissors"
    else:
        retVal = "Error"
    #endif    
    return retVal

    
def rpsls(player_choice):
    '''
    Function takes as input the string player_choice, which is one of "rock", "paper", "scissors", "lizard", or "Spock". 
    ''' 
    print ""    
    print "Player chooses", player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses", comp_choice
    res = (comp_number - player_number) % 5
    
    if (res == 0):
        print "Player and computer tie!"
    elif (1 <= res <= 2):
        print "Computer wins!" 
    elif (3 <= res <= 4):
        print "Player wins!"
    #endif    

# main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:        
    rpsls("rock")
    rpsls("lizard")
    rpsls("paper")
    rpsls("rock")
    rpsls("scissors")
    rpsls("Spock")

    



