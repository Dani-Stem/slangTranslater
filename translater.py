from tkinter import * 
from tkinter.ttk import *
from udpy import *
import random

client = UrbanClient()
   
master = Tk() 
master.geometry("400x100") 
master.title("Slang Translater")
  
label = Label(master, text = "  Plz enter the sentence or paragraph you want translated:") 
label.grid(row = 2, column = 2, sticky = W, pady = 2)

entry = Entry(master, width = 30)
entry.grid(row = 3, column = 2, pady = 2) 

def enter(evt):
    master1 = Toplevel(master)
    master1.geometry("400x100") 
    master1.title("Slang Translater")

    newlabel = ""

    userEntry = entry.get()

    if (userEntry != str('')):

        defs = client.get_definition(userEntry)
        newlabel = random.choice(defs)
    else:
        newlabel = "There is nothing to translate here "



    label1 = Label(master1, text=newlabel, wraplength=400)
    label1.grid(row = 2, column = 2, sticky = W, pady = 2)

button = Button(master, text = "Enter", command = enter)
button.grid(row=4,column=2)
master.bind('<Return>', enter)
  
mainloop()  
