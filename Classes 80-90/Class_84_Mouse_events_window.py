from tkinter import *


def mouse(event):
    print("Mouse coordinates: " + str(event.x) + ";"+str(event.y))
window = Tk()
'''
window.bind("<Button-1>",mouse) #left mouse click
window.bind("<Button-2>",mouse)#scroll wheel click
window.bind("<Button-3>",mouse)#right mouse click
window.bind("<ButtonRelease>",mouse)   # liberar o click
window.bind("<Enter>",mouse)#Enter the window  
window.bind("<Leave>",mouse)#Exit the window
'''
window.bind("<Motion>",mouse)#where the mouse moves

window.mainloop()