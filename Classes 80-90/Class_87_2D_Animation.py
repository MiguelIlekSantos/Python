from tkinter import *
import time

WIDTH = 400
HEIGHT = 400
vel_x  = 3
vel_y  = 3
window = Tk()

canvas =Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

background = PhotoImage(file="background.png")
resize = background.subsample(2,2)
background_canvas = canvas.create_image(0,0, image=resize,anchor=NW)

image = PhotoImage(file="UFO.png")
resized = image.subsample(2,2)
image_canvas = canvas.create_image(10,10, image=resized, anchor = NW)

image_width = resized.width()
image_height = resized.height()

while True:
    coords = canvas.coords(image_canvas)
    print(coords)
    if (coords[0]>= (WIDTH-image_width) or coords[0]<0):
        vel_x = -vel_x
    if (coords[1]>= (WIDTH-image_height) or coords[1]<0):
        vel_y = -vel_y
    canvas.move(image_canvas, vel_x,vel_y)
    window.update()
    time.sleep(0.01)

window.mainloop()