#!/usr/bin/env python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

import sys
import re
import os

"""
In this mission you should check if all elements in the given list are equal.

Input: List.

Output: Bool.

The idea for this mission was found on Python Tricks series by Dan Bader

Precondition: all elements of the input list are hashable 

"""

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

#============================================
# from typing import List, Any

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

# main entrance point:
if __name__ == '__main__':

    # print("Example:")
    # print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
