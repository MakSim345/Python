#!/usr/bin/python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

# ============================================================
# Taken from http://stackoverflow.com/questions/377017/test-if-executable-exists-in python
# http://stackoverflow.com/questions/3103589/how-can-i-easily-fixup-a-past-commit
# ============================================================
# SEP-2014
# ============================================================
# ============================================================

import os
from subprocess import call
import sys

def which(program):
    import os
    def is_exe(fpath):
        return os.path.exists(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None




# main entrance point:
if __name__ == "__main__":
    print ""
    
    if len(sys.argv) != 2:
        print "Usage: git fixup <commit>"
        sys.exit(1)

    git = which("git.exe")
    
    if not git:
        print "git-fixup: failed to locate git executable"
        sys.exit(2)

    call([git, "status"])    

    print ""
