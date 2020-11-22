from tkinter import *

root = Tk()
root.minsize(500, 200)

class sTui:
    def __init__(self, master):
        self.master = master
        master.title("Slang Translater")

        self.label = Label(master, text="Plz enter the sentence or paragraph you want translated:")
        #this doesnt work, idk why tho ??
        self.label.place(relx = 1.5, rely = 0.5, anchor = 'center')
        self.label.pack()

my_gui = sTui(root)
root.mainloop()


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
