#!/usr/bin/python
# -*-coding:cp1251 -*-
# -*- coding: utf8 -*-

#############################################################################
##
##
#############################################################################

import math
import os, sys
import traceback
import string
import collections

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


def decrypt(file_name):
    chars =  u"{}"
    f = open(file_name, 'rt')
    crypto_string = f.read().decode('utf8')
    decrypt_str = crypto_string 
    print crypto_string
    
    # print crypto_string[0]

    #res = sum(c != ' ' for c in crypto_string)
    #print res
    letters = collections.Counter(crypto_string)
    result = repr(letters).decode("unicode-escape")
    print result
    result = repr(letters).decode('utf8')
    print result
    
    decrypt_str = decrypt_str.replace(u"\u0432", "A")
    decrypt_str = decrypt_str.replace(u"\u0412", "A")
    decrypt_str = decrypt_str.replace(u"\u0440", "O")
    decrypt_str = decrypt_str.replace(u"\u0435", "H")
    decrypt_str = decrypt_str.replace(u"\u0443", "K")
    decrypt_str = decrypt_str.replace(u"\u0441", "M")
    decrypt_str = decrypt_str.replace(u"\u0447", "C")
    decrypt_str = decrypt_str.replace(u"\u044b", "B")
    decrypt_str = decrypt_str.replace(u"\u0438", "T")
    decrypt_str = decrypt_str.replace(u"\u043a", "E")
    decrypt_str = decrypt_str.replace(u"\u043b", "D")
    decrypt_str = decrypt_str.replace(u"\u0449", "3")
    decrypt_str = decrypt_str.replace(u"\u044c", "6")
    decrypt_str = decrypt_str.replace(u"\u0433", "W")
    print decrypt_str

    #for char in crypto_string:
        #chars[eval(char)] += 1

    #error_log_file = open(file_name, "r")
    #lines = error_log_file.readlines()

    f.close()


def freq_chars_in_str():

    crypto_string = "abasgaspoitaperi"
    # res[30] = {0}
    res = [ 0 for x in range(30)]
    print res

    print crypto_string
    for i in crypto_string:
        #print i
        #print ord(i) - ord('a')
        res[ord(i) - ord('a')] += 1
        #print "--"
        #if i in res:
        #    res.append(i)

    print res
    #print len(res)
    for i in range(len(res)):
        if res[i]:
            print chr(ord('a') + i) , res[i]
      # print i
        
    # print crypto_string[0]

if __name__ == "__main__":

    print "Main program start."
    print "----------------------"
    _file_to_read = "crypted_text.txt"
    # crypt()
    decrypt(_file_to_read)
    # print_the_table()
    # freq_chars_in_str()

    print "\n----------------------"
    print "Main program ends"



