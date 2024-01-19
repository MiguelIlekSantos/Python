from tkinter import *
from tkinter import colorchooser

def click():
    #color = colorchooser.askcolor()
    #colorhex = color[1]
    window.config(background=colorchooser.askcolor()[1])
window= Tk()

window.geometry("420x420")
button = Button(window, text="Choose color", command=click)
button.pack()

window.mainloop()