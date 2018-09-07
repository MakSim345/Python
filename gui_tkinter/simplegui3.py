from Tkinter import *

# Parameter box class
class ParamBox:
    bgcolor = "#104e8b"
    fgcolor = "#f5deb3"
    fontd = "Verdana 16"
    labelWidth = 15
    entryWidth = 5

    def __init__(self, parent, caption):
        self.caption = caption
        # Frame for label,entry and button
        self.fEntry = Frame( parent, border=2, pady=5, relief=RIDGE,
                             bg=self.bgcolor)
        self.fEntry.pack( side=TOP, fill=X)
        # Put parameter name to the leftmost position
        self.lb = Label( self.fEntry, text=self.caption,
                         width=self.labelWidth,
                         font=self.fontd,
                         anchor=W, justify=LEFT, fg=self.fgcolor,
                         bg=self.bgcolor)
        self.lb.pack( side=LEFT)
        
        self.entry = Entry( self.fEntry, font=self.fontd,
                            width=self.entryWidth)
        self.entry.pack( side=LEFT)
        # Set button shows the current contents in the entry
        self.btn = Button( self.fEntry, text="Set", font=self.fontd,
                           command=self.PrintParam)
        self.btn.pack( side=LEFT, padx=5)

        self.entry.bind("<Control-c>", self.entry.delete(0,END))

    # Print entry to console
    def PrintParam(self):
        print self.caption,": ",self.entry.get()

    # Clear entry
    def ClearEntry(self):
        self.entry.delete(0,END)


# Application
class GUIApp:
    title = "ICS IV-pump GUI"
    def __init__(self, master):
        # Parameter boxes' area on top
        self.fParams = Frame( master, relief="groove")
        self.fParams.master.title( self.title)
        self.fParams.pack( side=TOP)
        # Control buttons' area on below
        self.fControl = Frame( master)
        self.fControl.pack(side=TOP)

        self.bQuit = Button( self.fControl, text="Quit", command=master.quit)
        self.bQuit.pack(side=LEFT, pady=5)

        self.bClear = Button( self.fControl, text="Clear entries",
                              command=self.ClearEntries)
        self.bClear.pack(side=LEFT, pady=5, padx=2)


        # Populate the parameter boxes area        
        self.paramBoxList = []
        self.paramNames = ["Red wine bolus", "Kossubolus",\
                               "Coke bolus", "Pepsi bolus",\
                               "Limsabolus", "Lissee virtoo"]
        # Set up the desired parameter boxes
        for item in self.paramNames:
            self.paramBoxList.append( ParamBox( self.fParams, item))


    # Clear all entry boxes
    def ClearEntries(self):
        for item in self.paramBoxList:
            item.ClearEntry()


# start mainloop
if __name__ == '__main__':
   root = Tk()
   app = GUIApp(root)
   root.mainloop()


#eof
