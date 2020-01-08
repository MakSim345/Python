#!/usr/bin/python
# -*- coding: utf8 -*-

# ============================================================
# https://habr.com/ru/company/edison/blog/480884/ 
# ============================================================-

import sys, traceback
import PySimpleGUI27 as sg

def run_gui():
    layout = [
        [sg.Text('File 1'), sg.InputText(), sg.FileBrowse(),
        sg.Checkbox('MD5'), sg.Checkbox('SHA1')
        ],
        [sg.Text('File 2'), sg.InputText(), sg.FileBrowse(),
        sg.Checkbox('SHA256')
        ],
        [sg.Output(size=(88, 10))],
        [sg.Submit(), sg.Cancel()]  ]

    window = sg.Window('File Compare', layout)
    
    # The Event Loop
    while True:
        event, values = window.read()
        # print(event, values) #debug
        if event in (None, 'Exit', 'Cancel'):
            break
    


# main entrance point:
if __name__ == "__main__":

    print "Main program begins"
    print ""

    try:
       
        run_gui() 
    except:
        traceback.print_exc()
        # self.log.saveMessageToLog(a)
        print "Trigger Exception, traceback info forward to log file."
        traceback.print_exc(file=open("errlog.txt","a"))
        sys.exit(1) 

    print ""
    print "Main program ends"


