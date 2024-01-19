from tkinter import *
from tkinter import ttk
from tkinter import filedialog
def openfile():
    filepath = filedialog.askopenfilename(title="Open file okay?",
                                                                                filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    file = open(filepath, 'r')
    print(file.read())
    file.close()

def savefile():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes=[
                                        ("Textfile", ".txt"),
                                        ("Html files", ",html"),
                                        ("All files", ".*")]
                                    )
    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()

def cut():
    print("You Cutted something")
def copy():
    print("You Copied something")
def paste():
    print("You Pasted something")

window = Tk()
image_open = PhotoImage(file='Open.png')
image_save = PhotoImage(file='Save.png')
image_exit = PhotoImage(file='Exit.png')
##########Resized photo##############
Resized_open = image_open.subsample(10,10)
Resized_save = image_save.subsample(10,10)
Resized_exit = image_exit.subsample(10,10)

menubar = Menu(window)
window.config(menu=menubar)
window.geometry("200x200")
window.resizable(False,False)


filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Open",command=openfile,image=Resized_open,compound='left')
filemenu.add_command(label="Save",command=savefile,image=Resized_save,compound='left')
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quit,image=Resized_exit,compound='left')

editmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="paste",command=paste)

text = Text(window)
text.pack()

window.mainloop()