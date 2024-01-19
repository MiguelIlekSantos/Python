from tkinter import *

def reset_relief(button):
    button.config(state=NORMAL, relief=RAISED)

def check(event):
    if event.keysym in {'W', 'w'}:
        button_w.config(state=ACTIVE, relief=SUNKEN)
        window.after(100, lambda: reset_relief(button_w))
    elif event.keysym in {'A', 'a'}:
        button_a.config(state=ACTIVE, relief=SUNKEN)
        window.after(100, lambda: reset_relief(button_a))
    elif event.keysym in {'S', 's'}:
        button_s.config(state=ACTIVE, relief=SUNKEN)
        window.after(100, lambda: reset_relief(button_s))
    elif event.keysym in {'D', 'd'}:
        button_d.config(state=ACTIVE, relief=SUNKEN)
        window.after(100, lambda: reset_relief(button_d))

window = Tk()

window.bind("<Key>", check)

frame = Frame(window, background='black', bd=5, relief=RAISED)
frame.pack()

button_w = Button(frame, text="W", font=("Consola", 25), width=3)
button_w.pack(side=TOP)
button_a = Button(frame, text="A", font=("Consola", 25), width=3)
button_a.pack(side=LEFT)
button_s = Button(frame, text="S", font=("Consola", 25), width=3)
button_s.pack(side=LEFT)
button_d = Button(frame, text="D", font=("Consola", 25), width=3)
button_d.pack(side=LEFT)

window.mainloop()
