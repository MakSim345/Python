# from Tkinter import *
import tkinter as tk
import time as tm 


def display_time():
    current_time = tm.strftime('%H:%M:%S')
    clock_label['text'] = current_time
    my_window.after (1000, display_time)

# start mainloop
if __name__ == '__main__':
   my_window = tk.Tk()
   my_window.title ('Digital Clock')
   clock_label = tk.Label(my_window, font='ariel 80', bg='black', fg='red') 
   clock_label.grid(row=0, column=0)
   display_time()
   my_window.mainloop()
