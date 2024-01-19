from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    timelabel.config(text=time_string)

    day_String = strftime("%A")
    daylabel.config(text=day_String)

    date_String = strftime("%B %d  %Y")
    datelabel.config(text=date_String)

    window.after(1000, update)


window = Tk()

timelabel= Label(window, font=("Arial",35),fg="White", bg="black")
timelabel.pack()

daylabel= Label(window, font=("Ink Free",35))
daylabel.pack()

datelabel= Label(window, font=("Ink Free",35))
datelabel.pack()

update()

window.mainloop()

