from tkinter import *

def dosomething(event):
    print("You pressed {}".format(event.keysym))
    label.config(text=event.keysym)
windows = Tk()

windows.bind("<Key>", dosomething)
label = Label(windows, font=("Helvetica",25))
label.pack()

windows.mainloop()