import os
import sys
import re
import os
import sys

"""
Roman numerals come from the ancient Roman numbering system. 
They are based on specific letters of the alphabet which are combined to signify the 
sum (or, in some cases, the difference) of their values. 
The first ten Roman numerals are:
I, II, III, IV, V, VI, VII, VIII, IX, and X.
The Roman numeral system is decimal based but not directly positional and does not include a zero.
Roman numerals are based on combinations of these seven symbols:
Symbol Value
I 1 (unus)
V 5 (quinque)
X 10 (decem)
L 50 (quinquaginta)
C 100 (centum)
D 500 (quingenti)
M 1,000 (mille)

For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.
Input: A number as an integer.
Output: The Roman numeral as a string.
Precondition: 0 < number < 4000

"""
def checkio(_num_to_check):
    print "number:", _num_to_check
    _ret_val = "--"
    # TO_FIVE = ['ZERO', 'I','II','III','IV','V']
    TO_TEN =  ['ZERO', 'I','II','III','IV', 'V', 'VI','VII','VIII','IX','X']

    if (0 >= _num_to_check):
        return "Out of range"
    if (4000 <= _num_to_check):
        return "Out of range"

    if (1 <= _num_to_check <= 10):
        return TO_TEN[_num_to_check]
    
    if (11 <= _num_to_check <= 50):
        return TO_TEN[_num_to_check]
    
    #if (9 < _num_to_check < 20):
    #    a = _num_to_check % 5
    #    return SECOND_TEN[a]
    
        # print _ret_val
    return _ret_val
    
# main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    print "Main program start."
    print ""
    
    print checkio(0)
    print checkio(1)
    print checkio(2)
    print checkio(3)
    print checkio(3)
    print checkio(5)
    print checkio(6)
    print checkio(7)
    print checkio(8)
    print checkio(9)
    print checkio(10)
    print checkio(11)


    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert checkio(6) == 'VI', '6'
    #assert checkio(76) == 'LXXVI', '76'
    #assert checkio(499) == 'CDXCIX', '499'
    #assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print ""    
    print "Main program end."