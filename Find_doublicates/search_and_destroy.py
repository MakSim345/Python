import os, string
import glob
import shutil

def search_for_files(rootdir, file_extend):
    selected_files = []
    for root, subFolders, files in os.walk(rootdir):        
        for file in files:
            filePath = rootdir + '/' + file             
            ext = string.split(file, '.')
            if file_extend in ext:
                print "add file ", filePath
                selected_files.append(filePath)
            
    # print selected_files# filePath
    return selected_files

def copy_and_remove(file_list_array, destination_path):
    for each in file_list_array:
        print each
        shutil.copy(each, destination_path)
        os.remove (each)

