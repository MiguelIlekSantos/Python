from tkinter import *

# button = you click it, and it does stuff for u
count = 0
def click():
    global count # declares the count variable to be global instead of local
    count +=1
    print(count)

windows = Tk()

photo = PhotoImage(file='img.png')
resize = photo.subsample(10,10)
button = Button(windows,
                            text="Click Me",
                            command=click, #calls the function click
                            font=("Comic sans", 20,'bold'),
                            foreground="red",
                            bg="black",
                            activebackground="red",#sets the backround color when we click the button
                            activeforeground="black",# sets the text color when we click the button
                            state=ACTIVE,#sets the button to be active or deactivate
                            image=resize,
                            compound="top",
                            relief=RAISED,
                            bd=10)
button.pack()

windows.mainloop()
