from tkinter import *

def showMessage():
    print(firstnameentry.get()+"\n"+ lastnameentry.get()+"\n"+ Yearentry.get())

windows = Tk()

titlelabel = Label(windows, text="Enter your info", font=("Arial", 15)).grid(row=0, column=0, columnspan=2)
firstnamelabel = Label(windows, text="First name: ", width=10).grid(row=1, column=0)
firstnameentry = Entry(windows)
firstnameentry.grid(row=1, column=1)

lastnamelabel = Label(windows, text="Last name: ").grid(row=2, column=0)
lastnameentry = Entry(windows)
lastnameentry.grid(row=2, column=1)

Yearlabel = Label(windows, text="How old are you: ").grid(row=3, column=0)
Yearentry = Entry(windows)
Yearentry.grid(row=3, column=1)

submitbutton = Button(windows, text="Submit", command=showMessage).grid(row=4, column=0, columnspan=2)

windows.mainloop()
