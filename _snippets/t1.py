#!/usr/bin/python
# -*- coding: utf8 -*-
"""
A tool to perform a cross check for set of files:
 - Localization files from WebLocKit
 - Localization files from GIT repository

Comparation performs by script "cross_check.py".

File "textlist17.dtd" shall be present.
"""
import os
import string


def search_for_files(rootdir, file_extend):
    """
    make a list of files with given extention in given folder
    """
    # md={"roots":0, "sub_folders":0,"files": 0}
    # md={}
    selected_files = []
    # for root, sub_folders, files in os.walk(rootdir):
    for md in os.walk(rootdir):
        #print "root:", root
        #print "sub_folders:", sub_folders
        #print "files:", files
        # print md
        print "root:", md[0]
        print "sub_folders:", md[1]
        print "files:", md[2]

        for item_file in md[2]:
            file_path = os.path.join(md[0], item_file)
            ext = string.split(item_file, '.')
            if ext[1] in file_extend:
                selected_files.append(file_path)

    return selected_files


def main():
    """
    entry point
    """
    files_match = False
    file_extender = "xml"
    search_path_web = "web"
    search_path_git = "git"
    main_dict = {}

    array_web = search_for_files(search_path_web, file_extender)
    array_git = search_for_files(search_path_git, file_extender)
    print "array_git has: ", len(array_git)
    print "array_web has: ", len(array_web)

    for git_element in array_git:
        res = git_element.split('.')[0].split('-')[1]
        for web_element in array_web:
            if web_element.find(res) >= 0:
                main_dict[git_element] = web_element
                files_match = True

        if not files_match:
            print "Error: No match file for ", git_element

        files_match = False

    print main_dict
    #for _key in main_dict:
    #    exec_line = "cross_check.py " + _key + " " + main_dict[_key]
    #    print exec_line
    #    os.system(exec_line)

    print "main program end."

if __name__ == "__main__":
    main()

