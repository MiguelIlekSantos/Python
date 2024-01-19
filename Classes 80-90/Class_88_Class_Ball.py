class Ball:
    def __init__(self, canvas, x, y, diameter, vel_x, vel_y, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, diameter, diameter, fill=color)
        self.vel_x = vel_x
        self.vel_y = vel_y
    def move(self):
        coords = self.canvas.coords(self.image)
        #print(coords)
        if coords[2]>= self.canvas.winfo_width() or coords[0]<0:
            self.vel_x = -self.vel_x
        if coords[3]>= self.canvas.winfo_height() or coords[1]<0:
            self.vel_y = -self.vel_y
        self.canvas.move(self.image, self.vel_x, self.vel_y)