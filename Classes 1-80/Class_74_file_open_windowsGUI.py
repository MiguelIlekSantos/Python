from tkinter import *
from tkinter import filedialog
import locale

locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')

def openfile():
    filepath = filedialog.askopenfilename(title="Open file okay?",filetypes=(("text files","*.txt"), ("all files", "*.*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()
window =Tk()

button = Button(window,text="Open file", command=openfile)
button.pack()

window.mainloop()