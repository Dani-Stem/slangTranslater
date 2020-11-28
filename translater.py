from tkinter import * 
from tkinter.ttk import *
   
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

    words = {
        'doobie':['paper filled and rolled with marijuana'],
        'thot':['acronym for That Hoe Over There. meaning a promiscuous person'],
    }

    if (userEntry.find('doobie') != -1):
        definition = 'paper filled and rolled with marijuana'
        uIList = userEntry.split(' ')
        indexLen = len(uIList)
        index = uIList.index('doobie')
        index1 = uIList.index('doobie') + 1
        s=' '
        TransListBeg = (s.join(uIList[0:index]))
        TransListEnd = (s.join(uIList[index1:indexLen]))
        newlabel = (TransListBeg + ' ' + definition + ' ' + TransListEnd)
    elif (userEntry.find('thot') != -1):
        definition = 'acronym for That Hoe Over There. meaning a promiscuous person'
        uIList = userEntry.split(' ')
        indexLen = len(uIList)
        index = uIList.index('thot')
        index1 = uIList.index('thot') + 1
        s=' '
        TransListBeg = (s.join(uIList[0:index]))
        TransListEnd = (s.join(uIList[index1:indexLen]))
        print(TransListBeg + ' ' + definition + ' ' + TransListEnd)
    else:
        print('There is nothing to translate here: ' + userEntry)

    label1 = Label(master1, text=newlabel)
    label1.grid(row = 2, column = 2, sticky = W, pady = 2)

button = Button(master, text = "Enter", command = enter)
button.grid(row=4,column=2)
  
mainloop()  
