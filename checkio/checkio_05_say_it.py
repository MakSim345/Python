import os
import sys
import re
import os
import sys

"""
Stephen's speech module is broken. This module is responsible for his number pronunciation. 
He has to click to input all of the numerical digits in a figure, so when there are big 
numbers it can take him a long time. Help the robot to speak properly and increase his number 
processing speed by writing a new speech module for him. All the words in the string must be 
separated by exactly one space character. Be careful with spaces -- it's hard to see if you place 
two spaces instead one.
Input: A number as an integer.
Output: The string representation of the number as a string.
How it is used: This concept may be useful for the speech synthesis software or automatic reports systems. 
This system can also be used when writing a chatbot by assigning words or phrases numerical 
values and having a system retrieve responses based on those values.
Precondition: 0 < number < 1000

"""
FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["0", "1", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(_num_to_check):
    # print "number check:", _num_to_check
    
    if (0 > _num_to_check > 1000):
        return "Out of range"
        
    if( _num_to_check <= 9):        
        return FIRST_TEN[_num_to_check]

    if (9 < _num_to_check < 20):
        a = _num_to_check % 10
        return SECOND_TEN[a]

    if (20 <= _num_to_check < 100):
        _fir = int(_num_to_check / 10)
        _sec = _num_to_check % 10
        if (_sec == 0):
            return OTHER_TENS[_fir]
        else:
            return OTHER_TENS[_fir] + " " + FIRST_TEN[_sec]

    if (100 <= _num_to_check < 1000):
        _fir = int(_num_to_check / 100)
        _sec = int ((_num_to_check % 100 - _num_to_check % 10) / 10)
        _tre = _num_to_check % 10
        # print _fir , " " , _sec , " " , _tre
        _ret_val = FIRST_TEN[_fir] + " " +  HUNDRED

        if (_sec == 0):
             pass
        elif (_sec == 1):
             _ret_val = _ret_val + " " + SECOND_TEN[_tre]
             return _ret_val
        else:
             _ret_val = _ret_val + " " + OTHER_TENS[_sec]
        
        if (_tre == 0):
            pass
        else:
            _ret_val = _ret_val + " " + FIRST_TEN[_tre]
        
        # print _ret_val
        return _ret_val        
    
    return _num_to_check, " - False"
# main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    print "Main program start."
    print ""
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"     
    print ""    
    print "Main program end."