from tkinter import * 
from tkinter.ttk import *
   
master = Tk() 
master.geometry("300x100") 
master.title("Slang Translater")
  
label0 = Label(master, text = "Plz enter the sentence or paragraph you want translated:") 
label0.grid(row = 2, column = 2, sticky = W, pady = 2)

def get(event):
    print(event.widget.get())

entry0 = Entry(master, width = 40) 
entry0.grid(row = 3, column = 2, pady = 2) 
entry0.bind('<Return>', get)

button0 = Button(master, command=get)
button0.config(text="ENTER")
button0.grid(row=4,column=2)
  
mainloop() 


userInput = input('Plz enter the sentence or paragraph you want translated: ') 

words = {
    'doobie':['paper filled and rolled with marijuana'],
    'thot':['acronym for That Hoe Over There. meaning a promiscuous person'],
}

if (userInput.find('doobie') != -1):
    definition = 'paper filled and rolled with marijuana'
    uIList = userInput.split(' ')
    indexLen = len(uIList)
    index = uIList.index('doobie')
    index1 = uIList.index('doobie') + 1
    s=' '
    TransListBeg = (s.join(uIList[0:index]))
    TransListEnd = (s.join(uIList[index1:indexLen]))
    print(TransListBeg + ' ' + definition + ' ' + TransListEnd)
elif (userInput.find('thot') != -1):
    definition = 'acronym for That Hoe Over There. meaning a promiscuous person'
    uIList = userInput.split(' ')
    indexLen = len(uIList)
    index = uIList.index('thot')
    index1 = uIList.index('thot') + 1
    s=' '
    TransListBeg = (s.join(uIList[0:index]))
    TransListEnd = (s.join(uIList[index1:indexLen]))
    print(TransListBeg + ' ' + definition + ' ' + TransListEnd)
elif (userInput.find('ting') != -1):
    definition = 'current person of romantic and/or sexual interest'
    uIList = userInput.split(' ')
    indexLen = len(uIList)
    index = uIList.index('ting')
    index1 = uIList.index('ting') + 1
    s=' '
    TransListBeg = (s.join(uIList[0:index]))
    TransListEnd = (s.join(uIList[index1:indexLen]))
    print(TransListBeg + ' ' + definition + ' ' + TransListEnd)
elif (userInput.find('skrilla') != -1):
    definition = 'money'
    uIList = userInput.split(' ')
    indexLen = len(uIList)
    index = uIList.index('skrilla')
    index1 = uIList.index('skrilla') + 1
    s=' '
    TransListBeg = (s.join(uIList[0:index]))
    TransListEnd = (s.join(uIList[index1:indexLen]))
    print(TransListBeg + ' ' + definition + ' ' + TransListEnd)    
else:
    print('There is nothing to translate here: ' + userInput)
