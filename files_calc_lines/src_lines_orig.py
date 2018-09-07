#!/usr/bin/python
# -*- coding: cp1251 -*-
# скрипт для подсчета количества строк в исходниках проекта на Си
# (c) Alexander Belchenko, 2004
# http://onembedding.com/tools/python/code/
# $Id: src_lines.py,v 1.2 2005/02/02 22:25:11 bialix Exp $
#------------------------------------------------------------------------------

# укажите корневую папку с исходниками проекта
src_dir = r'j:\fujitsu\k1\src'

#------------------------------------------------------------------------------
import sys, os, os.path
from filename import FileName

#------------------------------------------------------------------------------
if __name__ == '__main__':
    
    qty_files = 0
    qty_c_files = 0
    qty_h_files = 0
    qty_asm_files = 0
    qty_inc_files = 0
    
    qty_lines_all = 0
    qty_c_lines = 0
    qty_h_lines = 0
    qty_asm_lines = 0
    qty_inc_lines = 0
    
    fname = FileName()
    
    for root, dirs, files in os.walk(src_dir):
        fname.dir = root
        for name in files:
            fname.name = name
            ext = fname.ext
            if ext in ['.c', '.h', '.asm', '.inc']:
                f = open(fname.path, 'rt')
                l = f.readlines()
                f.close()
                
                size = len(l)
                
                qty_files += 1
                qty_lines_all += size
                
                if ext == '.c':
                    qty_c_files += 1
                    qty_c_lines += size
                elif ext == '.h':
                    qty_h_files += 1
                    qty_h_lines += size
                elif ext == '.asm':
                    qty_asm_files += 1
                    qty_asm_lines += size
                elif ext == '.inc':
                    qty_inc_files += 1
                    qty_inc_lines += size
     
    print 'All files:', qty_files
    print 'All lines:', qty_lines_all
    print
    print 'C files:\t%d\tLines: %d' % (qty_c_files, qty_c_lines)
    print 'H files:\t%d\tLines: %d' % (qty_h_files, qty_h_lines)
    print 'ASM files:\t%d\tLines: %d' % (qty_asm_files, qty_asm_lines)
    print 'INC files:\t%d\tLines: %d' % (qty_inc_files, qty_inc_lines)
    
