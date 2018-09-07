import os
import sys
import re
import os
import sys

"""
You are given a text, which contains different english letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
Input: A text for analysis as a string (unicode for py2.7).
Output: The most frequent letter in lower case as a string.
Precondition:
The password contains only ASCII symbols.
0 < len(text) <= 10^5

"""


class net_data():
    def __init__(self):
        '''init'''
        self.date = 0
        self.total = 0.0
        self.status = 0


def checkio_2(els):
    a = 0
    for i in range(3):
        a = a + els[i]
    return a

def checkio(_string_to_check):
    print ("string to check:", _string_to_check)
    a = 0
    _dict = {}
    _max_n = 0
    _ret_letter = ''

    #ignore case:
    _string_to_check = _string_to_check.lower()

    # fill dictionary with letters and freq:
    for i in range(len(_string_to_check)):
        a = _string_to_check[i]
        if str.isalpha(a): # letters only!
            if (a in _dict):
                _dict[a] = _dict[a] + 1
            else:
                _dict[a] = 1
            #endif
        #endif
    #endfor

    for key in sorted(_dict):
        print ("%s: %s" % (key, _dict[key]))
        if _max_n < _dict[key]:
            _max_n = _dict[key]
            _ret_letter = key
            print ("New favourite: %s: %s" % (_max_n, _ret_letter))
        #endif
    #endfor

    return _ret_letter


def checkio_2(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)

def checkio_3(text):
    text = ''.join(i for i in text.lower() if i.isalpha())
    return max(set(text), key=text.count)

# main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    print "Main program start."
    print ""
    #number = input ("Enter a non-negative integer to take factorial of: ")
    #factorial_calc(number)

    # number = input ("Enter a non-negative integer to show max power of 2: ")
    print checkio('fn;lsfndasl;f naslkdnlkasdnfslahwemwjkrjkl;zcmk;lzcdkcslksdkseewme,')
    # print checkio('AAaooozkzkzk')

    print ""
    print "Main program end."
