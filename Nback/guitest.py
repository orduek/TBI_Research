#!/usr/bin/env python
import Tkinter as tk
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid()
        self.nBackButton=tk.Button(self, text="N-Back", command=self.run_nBack)
        self.nBackButton.grid()
        self.goNogoButton=tk.Button(self, text="Go-No Go", command=self.run_goNogo)
        self.goNogoButton.grid()
        self.corsiButton=tk.Button(self, text="Corsi Task", command=self.run_corsi)
        self.corsiButton.grid()
        self.label1=tk.Label(self, text="First Name")
        label1.grid()
        #Label(self, text="Last Name").grid(row=1)


    def run_nBack(self):
        os.system('/home/ord/Devel/Task/TBI_Research/Nback/nBack.py')
    def run_goNogo(self):
        os.system('/home/ord/Devel/Task/TBI_Research/gonogo/gonogo.py')
    def run_corsi(self):
        os.system('/home/ord/Devel/Task/TBI_Research/Corsi/corsi.py')

app = Application()
app.master.title('CreactKids Tasks')
app.mainloop()
