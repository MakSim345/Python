#!/usr/bin/python
# -*- coding: cp1251 -*-
# скрипт для подсчета количества строк в исходниках проекта на Си
# (c) Alexander Belchenko, 2004
# http://onembedding.com/tools/python/code/
# $Id: src_lines.py,v 1.2 2005/02/02 22:25:11 bialix Exp $
#------------------------------------------------------------------------------

# укажите корневую папку с исходниками проекта
# src_dir = r'C:\dev\esp_visual_studio'
src_dir = "C:\dev\esp_visual_studio"

#------------------------------------------------------------------------------
import sys, os, os.path
import string
# from filename import FileName

#------------------------------------------------------------------------------
if __name__ == '__main__':

    qty_files = 0
    qty_c_files = 0
    qty_cpp_files = 0
    qty_hpp_files = 0
    qty_h_files = 0
    qty_asm_files = 0
    qty_inc_files = 0

    qty_lines_all = 0
    qty_c_lines = 0
    qty_cpp_lines = 0
    qty_hpp_lines = 0
    qty_h_lines = 0
    qty_asm_lines = 0
    qty_inc_lines = 0

    # fname = FileName()
    selected_files = []

    for root, dirs, files in os.walk(src_dir):
        # fname.dir = root
        for name in files:
            # fname.name = name
            # ext = fname.ext
            filePath = os.path.join(root, name)
            #filePath = src_dir + '/' + name
            ext = string.split(name, '.')
            # print "File: ", name, " - ", ext, ext[-1]
            if ext[-1] in ['c', 'h', 'cpp', 'hpp', 'asm', 'inc']:
                # print "add file ", filePath
                selected_files.append(filePath)

                f = open(filePath, 'rt')
                l = f.readlines()
                f.close()

                size = len(l)
                qty_lines_all += size

                if ext[-1] == 'c':
                    qty_c_files += 1
                    qty_c_lines += size
                elif ext[-1] == 'cpp':
                    qty_cpp_files += 1
                    qty_cpp_lines += size
                elif ext[-1] == 'hpp':
                    qty_hpp_files += 1
                    qty_hpp_lines += size
                elif ext[-1] == 'h':
                    qty_h_files += 1
                    qty_h_lines += size
                elif ext[-1] == 'asm':
                    qty_asm_files += 1
                    qty_asm_lines += size
                elif ext[-1] == 'inc':
                    qty_inc_files += 1
                    qty_inc_lines += size

    #for each in selected_files:
    #    print each

    print 'All files:', qty_files
    print 'All lines:', qty_lines_all
    print
    print 'C files:\t%d\tLines: %d' % (qty_c_files, qty_c_lines)
    print 'CPP files:\t%d\tLines: %d' % (qty_cpp_files, qty_cpp_lines)
    print 'H files:\t%d\tLines: %d' % (qty_h_files, qty_h_lines)
    print 'HPP files:\t%d\tLines: %d' % (qty_hpp_files, qty_hpp_lines)
    print 'ASM files:\t%d\tLines: %d' % (qty_asm_files, qty_asm_lines)
    print 'INC files:\t%d\tLines: %d' % (qty_inc_files, qty_inc_lines)

