#!/usr/bin/python

from Tkinter import *

import random

class Fifteenth:
    def __init__(self,root):
        self.pieces =   [[0,1],[0,2],[0,3],[0,4], \
                    [0,5],[0,6],[0,7],[0,8], \
                    [0,9],[0,10],[0,11],[0,12], \
                    [0,13],[0,14],[0,15],[0,0]]
        self.field = []
        self.mix()
        for i in range(4):
            for j in range(4):
                if self.pieces[4*i+j][1] != 0:
                    but = Button(root,text=self.pieces[4*i+j][1])
                    but.bind("",lambda event=0,x=j,y=i: self.run(event,x,y))
                    but.grid(row=i,column=j,sticky=E+W+N+S)
                    self.pieces[4*i+j][0] = but
                else:
                    self.field = (j,i)

    def mix(self):
        for i in range(16):
            rand = random.randint(0,15)
            (self.pieces[i],self.pieces[rand]) = (self.pieces[rand],self.pieces[i])

    def run(self,event,x,y):
        if abs(x-self.field[0])==1 and y-self.field[1]==0 or abs(y-self.field[1])==1 and x-self.field[0]==0:
            newInd = 4*self.field[1]+self.field[0]
            (self.pieces[4*y+x],self.pieces[newInd]) = (self.pieces[newInd],self.pieces[4*y+x])
            self.pieces[newInd][0].grid(row=self.field[1],column=self.field[0], sticky=E+W+N+S)
            self.pieces[newInd][0].config()
            self.pieces[newInd][0].bind("",lambda event=0,x=self.field[0],y=self.field[1]: self.run(event,x,y))
            self.field = (x,y)

root = Tk()
Fifteenth(root)
root.mainloop()
