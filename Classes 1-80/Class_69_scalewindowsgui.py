from tkinter import *


def submit():
    print("The temperature is "+str(scale.get())+"  degrees C")

window = Tk()

window.geometry("300x600")

photo = PhotoImage(file='img.png')
window.iconphoto(True,photo)

window.title("Degrees")

hot_image = PhotoImage(file='hot_image.png')
resize_hot = hot_image.subsample(3,3)
hot_label = Label   (window,image=resize_hot)
hot_label.pack()

scale = Scale(window,
                       from_=100,
                       to= 0,
                       length=400,
                       width=20,
                       orient=VERTICAL ,
                       tickinterval=10, 
                       foreground="red",
                        background="black",
                        troughcolor="yellow",
                        highlightbackground='green',
                        activebackground='green')
scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

cold_image = PhotoImage(file='cold_image.png')
resize_cold = cold_image.subsample(3,3)
cold_label = Label   (window,image=resize_cold)
cold_label.pack()

button = Button(window,
                             text="submit",
                             command=submit,
                            foreground='lightblue',
                            activeforeground='black',
                            background='black',
                            activebackground='green')
button.pack()

window.mainloop()