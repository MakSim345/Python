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
This mission is the part of the set. Another one - Caesar cipher decriptor.

Your mission is to encrypt a secret message (text only, without special chars like "!", "&", "?" etc.) 
using Caesar cipher where each letter of input text is replaced by another that stands at a fixed distance. 
For example ("a b c", 3) == "d e f"
Input: A secret message as a string (lowercase letters only and white spaces)
Output: The same string, but encrypted
Precondition:
0 < len(text) < 50
-26 < delta < 26 
"""

import string
ALPHABET_LEN = 26

def to_encrypt(text, delta):
    #replace this for solution
    print (text, delta)
    res = ""
    a = (string.ascii_lowercase)
    for i in text:
       counter = 0
       # print "i=", i
       if i == ' ':
           res = res + ' '
       for cipher_char in a:
           if i == cipher_char:
               count_delta = (counter + delta) % ALPHABET_LEN
               # print "counter + delta = ", count_delta
               res = res + a[count_delta]
           counter = counter+1
           #endif
        #end_for
     #end_for
    print res           
    return res

if __name__ == '__main__':
    #print("Example:")
    #print(to_encrypt('abc', 10))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
