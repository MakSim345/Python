#!/usr/bin/env python

#############################################################################
## MAR-2015
## Get the name of current script with Python
#############################################################################

import os
import sys


if __name__ == "__main__":
    """
    Use __file__. 
    If you want to omit the directory part (which might be present), 
    you can use os.path.basename(__file__)."""
    print __file__
    print os.path.basename(__file__)

    
