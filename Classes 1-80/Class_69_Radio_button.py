from tkinter import *

#radio_button = similar to checkbox, but you can only select one from a group

food = ["pizza","hamburger","hotdog"]

def order():
    if(x.get()==0):
        print("You ordered pizza")
    elif(x.get()==1):
        print("You ordered hamburger")
    elif (x.get() == 2):
        print("You ordered hotdog")
    else:
        print('huh')

window = Tk()
window.geometry("420x420")
pizza = PhotoImage(file='pizza.png')
hamburger = PhotoImage(file='hamburger.png')
hotdog = PhotoImage(file='hotdog.png')
######Resizing images###########
resize_pizza = pizza.subsample(10,10)
resize_hamburger = hamburger.subsample(10,10)
resize_hotdog = hotdog.subsample(10,10)
###image in list####
food_img=[resize_pizza,resize_hamburger,resize_hotdog]
x=IntVar()

for i in range(len(food)):
    radiobutton = Radiobutton(window,
                                                   text=food[i], #ADDS text to radio button
                                                   variable=x,#group radiobutton together if they share the same variable
                                                   value=i,#assigns each radiobutton a different values
                                                   padx=20,
                                                   pady=10,
                                                   font=("inpact",10),
                                                   image = food_img[i],# adds image to radio button
                                                   compound='left', #adds imege and text (left side)
                                                   indicatoron=1,
                                                   width=375,
                                                   command=order)

    radiobutton.pack(anchor=W,side = 'top')

window.mainloop()