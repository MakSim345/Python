#!/usr/bin/env python

#############################################################################
## Question
## "How do you append directories to your Python path?"
## Answer
## Your path (i.e. the list of directories Python goes through to search for modules and files) 
## is stored in the path attribute of the sys module. Since path is a list, you can use the 
## append method to add new directories to the path. 
## 
##
#############################################################################


## For instance, to add the directory /home/me/mypy to the path, just do follow: 
import sys
sys.path.append("/home/me/mypy") 

import string
if __name__ == "__main__":
    print "OK"
    
