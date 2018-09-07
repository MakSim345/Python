#!/usr/bin/python

import os
import sys
import time
from random import Random
import string

def GenPasswd():
    newpasswd = ''.join( Random().sample(string.letters+string.digits, 12) )
    return newpasswd

print GenPasswd()
