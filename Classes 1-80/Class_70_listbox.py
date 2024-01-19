# listbox = A listing of selectable text items within it's own container

from tkinter import *

def submit():
    food = []
    for i in listbox.curselection():
        food.insert(i,listbox.get(i))
    print("You have ordered: " )
    for i in food:
        print(i)
def add():
    if entrybox.get() != "":
        listbox.insert(listbox.size(),entrybox.get())
        listbox.config(height=listbox.size())

def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window,
                             background='Black',
                             foreground='white',
                             font=("Arial",20,'bold'),
                             width=12,
                             selectmode=MULTIPLE)
listbox.pack()
listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"salad")
listbox.config(height=listbox.size())

entrybox = Entry(window,)
entrybox.pack()

add_button = Button(window,text='add',command=add)
add_button.pack()

delete_button = Button(window,text='delete',command=delete)
delete_button.pack()

submit = Button(window,
                            text='Submit',
                            command=submit)
submit.pack()
window.mainloop()