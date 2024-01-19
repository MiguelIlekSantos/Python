from tkinter import *
from tkinter import filedialog

def Savefile():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                                     filetypes=[
                                                         ("Textfile",".txt"),
                                                         ("Html files",",html"),
                                                         ("All files",".*")]
                                                    )
    filetext = str(text.get(1.0,END))
    file.write(filetext)
    file.close()


window = Tk()

text = Text(window)
text.pack()

button = Button(window, text="Save", command=Savefile)
button.pack()

window.mainloop()