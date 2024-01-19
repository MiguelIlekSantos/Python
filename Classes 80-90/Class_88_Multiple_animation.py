from tkinter import *
import time
from Class_88_Class_Ball import *
window = Tk()

WIDTH = 1100
HEIGHT = 600

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley = Ball(canvas, 0, 0, 100, 1, 1, "white")
tenis = Ball(canvas,0,0,50,4,3,"yellow")
basketball = Ball(canvas,0,0,125,8,7,"orange")

while True:
    volley.move()
    tenis.move()
    basketball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
