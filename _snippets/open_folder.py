#!/usr/bin/env python

#############################################################################
##
##
#############################################################################

import string
import subprocess
import sys

if sys.platform == 'darwin':
    def openFolder(path):
        subprocess.check_call(['open', '--', path])
elif sys.platform == 'linux2':
    def openFolder(path):
        subprocess.check_call(['gnome-open', '--', path])
elif sys.platform == 'win32':
    def openFolder(path):
        subprocess.check_call(['explorer', path])

if __name__ == "__main__":    
    openFolder("D:\dev")
