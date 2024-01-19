#Canvas = widget that is used to draw graphs, plot, images in a windows

from tkinter import *

windows = Tk()


canvas = Canvas(windows,width=500, height=500,)
'''
canvas.create_line(0,0,500,500,fill="blue",width=5)
canvas.create_line(0,500,500,0,fill="red",width=5)
canvas.create_rectangle(200,200,350,350)
'''
'''
points = [250,0,500,500,0,500]
canvas.create_polygon(points,fill="yellow",outline="red",width=5)
'''

#canvas.create_arc(0,0,500,500,fill="blue",style=PIESLICE, start=-90)

################Poke----Ball############################
canvas.create_arc(0, 0, 500, 500,fill = "red", extent=180,width=10)
canvas.create_arc(0, 0, 500, 500,fill = "white",start=180, extent=180,width=10)
canvas.create_oval(190, 190, 320, 320, fill="white",width=10)

canvas.pack()
windows.mainloop()