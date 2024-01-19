from tkinter import *

# widgets = GUI elements: buttons, textboxs, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk()
# instantiate an instance of windows
window.geometry("420x420")
window.title("Created")

icon = PhotoImage(file='img.png')
window.iconphoto(True,icon)

window.config(background="Green")

window.mainloop() # place windows on computer screen, listen    for events
