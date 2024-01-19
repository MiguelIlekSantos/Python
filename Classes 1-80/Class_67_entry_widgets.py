from tkinter import *

# entry_widjets = textbox that accepts a single line of user input

def Submit():
    username=entry.get()
    print("Hello "+username)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)


windows = Tk()
windows.resizable(False,False)
entry = Entry(windows,
                        font=("Comic sans",20,'bold'),
                        foreground="blue",
                        relief=RAISED,
                        bd=10,
                        bg="black")
entry.pack(side=LEFT)

exit_button = Button(text="Exit",
                     command=exit,
                     foreground="blue",
                     bg="lightblue",
                     relief=RAISED,
                     bd=10)

exit_button.pack(side=RIGHT)

submit_button = Button(windows,
                            font=("Arial",10,'italic'),
                            text="submit",
                            command=Submit,
                            foreground="blue",
                            bg="lightblue",
                            relief=RAISED,
                            bd=10)
submit_button.pack(side=RIGHT)

delete_button = Button(windows,
                            font=("Arial",10,'italic'),
                            text="Delete",
                            command=delete,
                            foreground="blue",
                            bg="lightblue",
                            relief=SUNKEN,
                            bd=10,
                            activebackground="yellow",
                            activeforeground="red")
delete_button.pack(side=RIGHT)

back_space_button = Button(windows,
                            font=("Arial",10,'italic'),
                            text="Backspace",
                            command=backspace,
                            foreground="blue",
                            bg="lightblue",
                            relief=RAISED,
                            bd=10)
back_space_button.pack(side=RIGHT)

windows.mainloop()