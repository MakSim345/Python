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
def check_horizontal(matrix):
    # print "string to check:", matrix
    ret_value = False

    for line in matrix:
        prev_num = 0
        match_ctr = 0
        for i in line:
            # print i, prev_num, match_ctr
            if i == prev_num:
                match_ctr = match_ctr + 1
                if match_ctr >= 3:
                    print "MATCH! - hor", line
                    ret_value = True
            else:
                match_ctr = 0
            prev_num = i
    return ret_value

def check_vertical(matrix):
    ret_value = False
    print "vert: Matrix has:", len(matrix)
    for num in range(len(matrix[0])):
        i = matrix[0][num]
        print "to check:", i
        prev_num = i
        match_ctr = 0
        for j in range(1, len(matrix)):
            i = matrix[j][num]
            print j, "- ", i, " compare to: ", prev_num
            if i == prev_num:
                match_ctr = match_ctr + 1
                if match_ctr >= 3:
                    print "MATCH! - vert"
                    ret_value = True
            else:
                match_ctr = 0
            prev_num = i
    
    return ret_value

def check_diagonal(matrix):    
    print "string to check:", matrix
    ret_value = False
    new_matrix = []    
    super_matrix = []
    row_num = len(matrix)
    col_num = len(matrix[0])
    #print "matrix has", row_num, "rows"
    #print "matrix has", col_num, "columns"
   
    for i in range(3, row_num):
        #print i, "-test"
        a = i
        for j in range(i+1):
            tmp = matrix[a][j]
            # print "tmp", a, j, tmp
            new_matrix.append(tmp)
            a=a-1
        print new_matrix
        super_matrix.append(new_matrix)
        new_matrix = []
    
    for i in range(1, row_num-3):
        # print i, "-test"
        a = i
        for j in range(row_num-i):
            tmp = matrix[a][(col_num-1)-j]
            # print "tmp", a, j, tmp
            new_matrix.append(tmp)
            a=a+1
        print new_matrix
        super_matrix.append(new_matrix)
        new_matrix = []    

    for i in range(row_num-3):
        #print i, "-test"
        a = i
        for j in range(col_num-i):
            #print "a, j:", a, j
            tmp = matrix[a][j]
            #print "tmp:", tmp
            new_matrix.append(tmp)
            a=a+1
        print new_matrix
        super_matrix.append(new_matrix)
        new_matrix = []
    
    for i in range(3, row_num):
        #print i, "-test"
        a = i
        for j in range(i+1):
            tmp = matrix[a][(col_num-1)-j]
            #print "tmp", a, j, tmp
            new_matrix.append(tmp)
            a=a-1
        print new_matrix
        super_matrix.append(new_matrix)
        new_matrix = []

    ret_value = check_horizontal(super_matrix)
    
    #new_matrix = []
    #new_matrix.append(matrix[row_num-4][col_num-1])
    #new_matrix.append(matrix[row_num-3][col_num-2])
    #new_matrix.append(matrix[row_num-2][col_num-3])
    #new_matrix.append(matrix[row_num-1][col_num-4])
    #print "unittest:", new_matrix
    
    return ret_value

def checkio(matrix):
    # print "string to check:", matrix
    ret_value = False

    if check_horizontal(matrix):
        return True

    if check_vertical(matrix):
        return True

    if check_diagonal(matrix):
        return True

    print "return", ret_value
    return ret_value

# main entrance point:
if __name__ == '__main__':

    # print("Example:")
    # print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    
    assert checkio([
        [2,7,6,2,1,5,2,8,4,4],
        [8,7,5,8,9,2,8,9,5,5],
        [5,7,7,7,4,1,1,2,6,8],
        [4,6,6,3,2,7,6,6,5,1],
        [2,6,6,9,8,5,5,6,7,7],
        [9,4,1,9,1,3,7,2,3,1],
        [5,1,4,3,6,5,9,3,4,1],
        [6,5,5,1,7,7,8,2,1,1],
        [9,5,7,8,2,9,2,6,9,3],
        [8,2,5,7,3,7,3,8,6,2]
        ]) == False, "Nothing here"
    
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"

    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 9, 7, 3, 1, 5],
        [2, 3, 9, 2, 5, 1],
        [1, 1, 1, 9, 1, 4],
        [4, 6, 5, 1, 9, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"

    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"

    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"

    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"

    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [4, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"

    assert checkio([
        [4, 5, 6, 3, 4, 4],
        [3, 2, 2, 6, 2, 1],
        [1, 3, 5, 6, 3, 1],
        [5, 1, 4, 6, 3, 2],
        [3, 4, 2, 6, 2, 3],
        [3, 5, 4, 2, 4, 5]
        ]) == True, "Vertical"

