#!/usr/bin/env python
from Tkinter import *
import os

def run_nBack():
    os.system('/home/ord/Devel/Task/TBI_Research/Nback/nBack.py')
def run_goNogo():
    os.system('/home/ord/Devel/Task/TBI_Research/gonogo/gonogo.py')
def run_corsi():
    os.system('/home/ord/Devel/Task/TBI_Research/Corsi/corsi.py')
def run_test():
    os.system('/home/ord/Devel/Task/TBI_Research/Nback/test2.py')

master = Tk()
Label(master, text="Subject No.").grid(row=0)
Label(master, text="Subject Age").grid(row=1)


e1 = Entry(master)
e2 = Entry(master)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b=e1.get()

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='nBack', command=run_nBack).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Go-NoGo', command=run_goNogo).grid(row=4, column=0, sticky=W, pady=4)
Button(master, text='Corsi', command=run_corsi).grid(row=4, column=1, sticky=W, pady=4)
Button(master, text="test",command=run_test).grid(row=4, column=2, sticky=W, pady=4)

mainloop()
