#!/usr/bin/python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-
# ============================================================
#
#
# ============================================================
#
# Author:         YS
#
# ============================================================
# Description: make printscreen and save to Dropbox folder.
# Need 'wx' to be installed.
# for copy use 'shutil'
# ============================================================
import os
import wx
import time
import shutil


def getScreenByWx(_filename = 'screenshot.png'):     
    # this do not work, always error:
    # wx.App()  # Need to create an App instance before doing anything
    app = wx.PySimpleApp() # this one works, but complains

    screen = wx.ScreenDC()
    size = screen.GetSize()
    bmp = wx.EmptyBitmap(size[0], size[1])
    mem = wx.MemoryDC(bmp)
    mem.Blit(0, 0, size[0], size[1], screen, 0, 0)    
    del mem  # Release bitmap

    bmp.SaveFile(_filename, wx.BITMAP_TYPE_PNG)

def copy_file_to_dropbox(file_name, destination_path):    
    print "file to remove here:", file_name
    shutil.copy(file_name, destination_path)
    os.remove(file_name)

if __name__ =='__main__':
    
    destination_path  = "D:\Dropbox\images"        
    screenshot_filename = time.strftime("%Y%m%d-%H%M%S")+'.png'
    print "result file: " , screenshot_filename

    getScreenByWx(screenshot_filename)
    copy_file_to_dropbox(screenshot_filename, destination_path)

