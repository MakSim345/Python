#!/usr/bin/env python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

import sys
import re
import os

"""
You are given an expression with numbers, brackets and operators. For this task only the brackets matter. Brackets come in three flavors: "{}" "()" or "[]". Brackets are used to determine scope or to restrict some expression. If a bracket is open, then it must be closed with a closing bracket of the same type. The scope of a bracket must not intersected by another bracket. In this task you should make a decision, whether to correct an expression or not based on the brackets. Do not worry about operators and operands.

Input: An expression with different of types brackets as a string (unicode).

Output: A verdict on the correctness of the expression in boolean (True or False).

Precondition:
There are only brackets ("{}" "()" or "[]"), digits or operators ("+" "-" "*" "/").
0 < len(expression) < 10^3
"""

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
def checkio(expression):
    print "string to check:", expression
    ret_value = True

    stack_open = []
    array_of_open = ['{', '(', '[']
    array_of_close = ['}', ')', ']']

    dict_all = {'{':'}', '(':')', '[':']', '$':'$'}
    a = {}
    b = {}

    res_a = []
    res_b = []

    for i in expression:
        # print "handle", i
        if i in array_of_open:
            stack_open.append(i)
            if i in a:
                a[i] = a[i]+1
            else:
                a[i] = 1
            #endif
        #endif
        if i in array_of_close:
            #print "--------------"
            #print "current_close:", i            
            if stack_open:
                current_open = stack_open.pop()
            else:    
                current_open = '$'
            #print "need:", dict_all[current_open]
            #print "current_open:", current_open            

            if not i == dict_all[current_open]:
                print i, "--------not equal to", dict_all[current_open]
                ret_value = False
                print "return", ret_value
                return ret_value
            #else:
            #    print i, "IS equal to", dict_all[current_open]
            #endif
            if i in b:
                b[i] = b[i]+1
            else:
                b[i] = 1
            #endif
        #endif
     #end_for
    
    a2 = dict(sorted(a.items()))
    b2 = dict(sorted(b.items()))

    for key, val in a2.items():
        print (key, val)
        res_a.append(val)
    #endfor

    for key, val in b2.items():
        print (key, val)
        res_b.append(val)
    #endfor

    print (res_a)
    print (res_b)
    
    if (not res_a and res_b) or (not res_b and res_a):
        ret_value = False
        print "Empty one array. Return", ret_value
        return ret_value

    for i in range(len(res_a)):
        if not res_a[i] == res_b[i]:
            # print res_a[i], "not equal to", res_b[i]
            ret_value = False
    print "return", ret_value
    return ret_value

# main entrance point:
if __name__ == '__main__':

    # print("Example:")
    # print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio("{") == False, "One is redundant"
    assert checkio("(((1+(1+1))))]")== False, "One is redundant"
    assert checkio("(((([[[{{{3}}}]]]]))))")== False, "One is redundant"
    assert checkio("[(3)+(-1)]*{3}") == True, "Real result"
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"

