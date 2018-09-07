#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#
#

import sys
import os

from math import *
from Tkinter import *
from tkMessageBox import *

#
#
import serial
SERIAL_PORT = 'COM4'
SERIAL_SPEED = 38400
# SERIAL_SPEED = 9600

codepage = 'utf-8'
debug = 0
data_file = 't.txt'


class App:
    age=0
    data0=0
    data1=0
    itable=[]

    def __init__(self):
        self.window = Tk()
        self.window.title("Oscilloscope")
        self.window.resizable(0, 0)

        self.workspace = Frame(self.window, relief=FLAT)
        self.workspace.grid(row=0, column=0)

        self.G = Canvas(self.window, borderwidth=2, relief=GROOVE)
        self.G.grid(row=1, column=0)
        self.G.config(width=500, height=500, background="black")

        self.gbtn = Button(self.workspace, text=u"Start")
        self.gbtn["command"] = self.draw
        self.gbtn.grid(row=3, column=10)

        self.gbtn = Button(self.workspace, text=u"Serial")
        self.gbtn["command"] = self.get_data_from_com
        self.gbtn.grid(row=3, column=11)

        self.gbtn = Button(self.workspace, text=u"File")
        self.gbtn["command"] = self.draw_file
        self.gbtn.grid(row=3, column=12)

        self.gbtn = Button(self.workspace, text=u"Quit")
        self.gbtn["command"] = self.quit
        self.gbtn.grid(row=3, column=13)

        self.draw_axis()
        #self.get_data(data_file)
        #self.draw()
        self.window.mainloop()

    def quit(self):
        self.window.destroy()

    def draw(self):
        fml = str("sin(x)")
        x1 = float("-10")
        x2 = float("10")
        y1 = float("-10")
        y2 = float("10")

#        if x1>=x2:
#            showerror("Error", u"StartX")
#            return

        dx = (x2-x1)/500
        dy = (y2-y1)/500
        coords = []

        try:
            x = x1
            y = eval(fml)
        except SyntaxError:
            showerror("Error", u"!")
            return
        except:
            pass

        for i in range(500):
            x = x1 + dx*i
            try:
                y = eval(fml)
            except:
                j = None
            else:
                j=500-500*(y-y1)/(y2-y1)
            coords.append(j)

        self.G.delete("all")

        ax = 500*(-x1)/(x2-x1)
        self.G.create_line(ax, 0, ax, 500, fill='brown')
        ay = 500 - 500*(-y1)/(y2-y1)
        self.G.create_line(0, ay, 500, ay, fill='brown')

        for i in range(499):
            a = coords[i]
            b = coords[i+1]
            if a!=None and b!=None:
                self.G.create_line(i,a,i+1,b,fill="green")

    def draw_file(self):
        self.get_data(data_file)
        return

    def draw_axis(self):
        x1 = float("-10")
        x2 = float("10")
        y1 = float("-10")
        y2 = float("10")
        ax = 500*(-x1)/(x2-x1)
        self.G.create_line(ax, 0, ax, 500, fill='brown')
        ay = 500 - 500*(-y1)/(y2-y1)
        self.G.create_line(0, ay, 500, ay, fill='brown')
        return

    def drawdata(self,data):
        #print data
        #lid = self.G.create_line(0,0,500,100,fill="white")
        x1 = float("-10")
        x2 = float("10")
        y1 = float("-10")
        y2 = float("10")

        center=250
        j=data-150

        self.itable.append(j)


        i = self.age
        a = self.itable[i-1]
        b = self.itable[i]

        #print i-1,a
#        print i,b
        #if a!=None and b!=None:
        lid=self.G.create_line(i-1+center,a,i+center,b,fill="green")
        #self.G.create_line(0,0,i,b,fill="white")
        #print lid
        self.age=self.age+1
        print data
        return None

    def get_data(self,file_name_):
        #
        # read data from file
        #
        self.G.delete("all")
        self.draw_axis()

        i=0
        j=0
        try:
            f=open(file_name_,'r')
            print "[i] open "+file_name_,
        except IOError:
            print "[!] Cant open file "+file_name_
            return -1
        print "..ok"
        lines=len(f.readlines())
        f.seek(0)
        print lines
        data=0
        for l in range(0,lines):
            data=float(f.readline())
            self.drawdata(data)
        f.close()

        self.age=0
        self.itable=[]

        return None

    def get_data_from_com(self):
        self.G.delete("all")
        self.draw_axis()
        self.age=0

        ser = serial.Serial(SERIAL_PORT, SERIAL_SPEED)

        # while 1:
        for i in range(0, 10):
            # s = ser.read()
            s = ser.readline().strip()
            print str(i), " - ", s, "\n"
            if str.isalnum(s):
                self.drawdata(float(s))

        return None

#App()

#-----------------------------------------
#
# begin here :)
#

def main():
    print "[i] Start testing..."
    app = App()

    print "[i] done."
    return None

if __name__ == "__main__":
    main()