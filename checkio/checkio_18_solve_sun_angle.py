#!/usr/bin/env python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

import sys
import re
import os

def checkio_1(expression):
    print ("string to check:", expression)
    a = 0
    _dict = {}
    _max_n = 0
    _ret_letter = ''

    #ignore case:
    expression = expression.lower()

    # fill dictionary with letters and freq:
    for i in range(len(expression)):
        a = expression[i]
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

def count_words(text, words):
    """ text: str, words: set
        output: int """
    ret_value = 0
    print "Input text:", text
    text_to_handle = text.lower()
    for i in words:
        print i
        if i in text_to_handle:
            print i ," is in text!"
            ret_value = ret_value + 1
    return ret_value

def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    if not line:
        return 0

    a = {}
    # print line
    curr_char = ''
    prev_char = ''
    chr_arr = list(line)
    for i in chr_arr:
        curr_char = i

        if curr_char == prev_char:
            if i in a:
                a[i] = a[i]+1
        else:
            a[i] = 1
        #endif
        prev_char = i

    print a
    max_key = max(a, key=lambda k: a[k])
    print "return:", a[max_key]
    return a[max_key]

def all_the_same(List):
    # print List
    a = {}
    prev_hash = 0
    first_elm = True
    for i in List:
        # print i, hash(i)
        if first_elm:
            first_elm = False
            prev_hash = hash(i)
        else:
            if not prev_hash == hash(i):
                return False
    return True


#============================================
"""
Every true traveler must know how to do 3 things: fix the fire,
find the water and extract useful information from the nature around him. 
Programming won't help you with the fire and water, 
but when it comes to the information extraction - it might be just the thing you need.

Your task is to find the angle of the sun above the horizon knowing the time of the day. 
Input data: the sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees.
At 12:00 PM the sun reaches its zenith, which means that the angle equals 90 degrees.
6:00 PM is the time of the sunset so the angle is 180 degrees. 
If the input will be the time of the night (before 6:00 AM or after 6:00 PM), 
your function should return - "I don't see the sun!".

Input: The time of the day.
Output: The angle of the sun, rounded to 2 decimal places.
Precondition:
00:00 <= time <= 23:59 
"""

def sun_angle(time):
    #replace this for solution
    print time   
    hours = int (time[0]+time[1])
    minutes = int (time[3]+time[4])
    
    if hours < 6 or hours >= 18:
        ret_val =  "I don't see the sun!"
        print ret_val
        return ret_val

    hrs_grad = {}
    morning = 7
    morning_grad = 15
    for i in range(12):
        hrs_grad[morning] = morning_grad
        morning_grad = morning_grad + 15
        morning = morning + 1
    
    if minutes == 0:
        ret_val = hrs_grad[hours]
    else:
        ret_val = hrs_grad[hours] + minutes * 0.25

    print int(ret_val)
    return int(ret_val)

if __name__ == '__main__':
    # print("Example:")
    # print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("10:25") == 66
    assert sun_angle("18:01") == "I don't see the sun!"
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
