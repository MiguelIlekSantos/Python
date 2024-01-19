from tkinter import *

def display():
    if (x.get() == 1):
        print(" You agree")
    else:
        print("You don't agree")
window = Tk()
window.geometry("420x420")
x = IntVar()
photo = PhotoImage(file='phyton.png')
resize = photo.subsample(30,30)
checkbutton = Checkbutton(window,
                                                text="I agree the terms to play this games",
                                                variable=x,
                                                onvalue=1,
                                                offvalue=0,
                                                command=display,
                                                bg="black",
                                                foreground="white",
                                                activeforeground="black",
                                                activebackground="green",
                                                padx=1,
                                                pady=1,
                                                image=resize,
                                                compound="left")
checkbutton.pack()

window.mainloop()