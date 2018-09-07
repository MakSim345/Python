#!/usr/bin/python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

#############################################################################
##
##
#############################################################################

import math
import os, sys
import traceback
import string

def encrypt():
    c = "LXFOPVEFRNHR"  # шифрованое сообщение
    k = "LEMON"  # ключ

    k *= len(c) // len(k) + 1  # подгоняем ключ
    m = ''.join([chr((ord(j) - ord(k[i])) % 26 + ord('A')) for i, j in enumerate(c)])  # расшифровываем
    print(m) # ATTACKATDAWN
    

def crypt(key='', message=''):
    #msg = "ATTACKATDAWN"  # message
    #k = "LEMON"  # the key
    msg = "THESUNANDTHEMANINTHEMOON"  # message
    k = "KING"  # the key
    
    k *= len(msg) // len(k) + 1  # multiply key to the message.
    
    c = ''.join([chr((ord(j) + ord(k[i])) % 26 + ord('A')) for i, j in enumerate(msg)]) 

    for i, j in enumerate(msg):
        _num = (ord(j) + ord(k[i])) % 26 + ord('A')
        _char = chr(_num)
        #print i, " - ", j, ":", _char
        print "-", j, ord(j), "+", k[i], ord(k[i]), "=", _char, ord(_char)

    print(c) # LXFOPVEFRNHR

def crypto_task():
    cr_text= 'wubefiqlzurmvofehmymwt'


def print_the_table():
    ''' print the table of the shifted alphabets '''
    a = string.ascii_lowercase
    m_arr = []
    new_arr = []
    for i in range(len(a)):
        # print a[i]
        m_arr.append(a[i])

    # print m_arr
    for i in range(len(a)):
        print m_arr
        m_arr.insert(len(a), m_arr.pop(0))


if __name__ == "__main__":    

    print "Main program start."
    print "----------------------"
    
    crypt()
    # print_the_table()
        
    print "----------------------"
    print "Main program ends"



