from tkinter import *

'''
def move(event):
    if event.keysym == "w" or event.keysym == "W":
        if label.winfo_y() != 0:
            label.place(x = label.winfo_x(), y = label.winfo_y()-1)
    elif event.keysym == "a" or event.keysym == "A":
        if label.winfo_x() != 1:
            label.place(x=label.winfo_x()-1, y=label.winfo_y())
    elif event.keysym == "s" or event.keysym == "S":
        if label.winfo_y() != 445:
            label.place(x=label.winfo_x(), y=label.winfo_y() + 1)
    elif event.keysym == "d" or event.keysym == "D":
        if label.winfo_x() != 445:
            label.place(x=label.winfo_x()+1, y=label.winfo_y() )

window =Tk()
window.geometry("500x500")
window.resizable(False,False)

window.bind("<Key>",move)

image =PhotoImage(file="background.png")
resized = image.subsample(20,20)

label = Label(window, image=resized)
label.place(x=1,y=0)

window.mainloop()'''



################Parte Canvas######################

def move(event):
    if event.keysym == "w" or event.keysym == "W":
        canvas.move( myimage,0,-1)
    elif event.keysym == "a" or event.keysym == "A":
        canvas.move(myimage, -1, 0)
    elif event.keysym == "s" or event.keysym == "S":
        canvas.move(myimage, 0, 1)
    elif event.keysym == "d" or event.keysym == "D":
        canvas.move(myimage, 1, 0)

window = Tk()

window.bind("<Key>",move)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

photo = PhotoImage(file="img.png")
resized = photo.subsample(30,30)

myimage = canvas.create_image(0,0,image=resized,anchor=NW)
window.mainloop()
