from tkinter import * 
from tkinter.ttk import *
from udpy import UrbanClient

client = UrbanClient()
   
master = Tk() 
master.geometry("300x100") 
master.title("Slang Translater")
  
label = Label(master, text = "Plz enter the sentence or paragraph you want translated:") 
label.grid(row = 2, column = 2, sticky = W, pady = 2)

entry = Entry(master, width = 40)
entry.grid(row = 3, column = 2, pady = 2) 

def enter():
    master1 = Toplevel(master)
    master1.geometry("300x100") 
    master1.title("Slang Translater")

    newlabel = ""

    userEntry = entry.get()

    if (userEntry == str('netflix and chill')):

        defs = client.get_definition('netflix and chill')
        newlabel = defs
    else:
        print('There is nothing to translate here: ' + userEntry)



    label1 = Label(master1, text=newlabel)
    label1.grid(row = 2, column = 2, sticky = W, pady = 2)

button = Button(master, text = "Enter", command = enter)
button.grid(row=4,column=2)
  
mainloop()  
