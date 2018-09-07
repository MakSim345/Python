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
# Description: 
# ============================================================
import os
import wx
import time

class applicationName(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Title', size=(300,200))
        panel = wx.Panel(self)
        
        box = wx.TextEntryDialog(None, "How old are you?", "Title", "default text")
        
        screen = wx.ScreenDC()
        size = screen.GetSize()
        print "size = ", size

        #if box.ShowModal() == wx.ID_OK:
        #    answer = box.GetValue()            


def getScreenByWx():    
    print "start wx.App()"
    # wx.App()  # Need to create an App instance before doing anything
    app = wx.PySimpleApp()
    screen = wx.ScreenDC()
    size = screen.GetSize()
    bmp = wx.EmptyBitmap(size[0], size[1])
    mem = wx.MemoryDC(bmp)
    mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
    del mem  # Release bitmap
    bmp.SaveFile('screenshot.png', wx.BITMAP_TYPE_PNG)

if __name__ =='__main__':
    
    getScreenByWx()

    #app = wx.PySimpleApp()
    #frame = applicationName(parent=None, id=-1)
    #frame.Show()
    #frame.Close()
    # app.MainLoop()
    # app.ExitMainLoop()

    
