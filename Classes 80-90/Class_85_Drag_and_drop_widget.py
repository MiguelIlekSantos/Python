from tkinter import *

def drag(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

window = Tk()

label = Label(window, text="Drag", bg="yellow",foreground="blue",height=4,width=10)
label.place(x=0,y=0)

label_2 = Label(window, text="Drag", bg="yellow",foreground="blue",height=4,width=10)
label_2.place(x=110,y=110)

label.bind("<Button-1>", drag)
label.bind("<B1-Motion>", drag_motion)

label_2.bind("<Button-1>", drag)
label_2.bind("<B1-Motion>", drag_motion)

window.mainloop()