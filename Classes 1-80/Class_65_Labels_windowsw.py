from tkinter import *
#label = an area widgets that holds text and/or an image within a window

window = Tk()

photo=PhotoImage(file='img.png') #defines the photo to put in label
resized = photo.subsample(10,10)#helps to put the size of img u want
window.geometry('500x500')  #defines the size of windows while starting
window.title("Im the main character")#changes the title of the window that is created
window.iconphoto(True,photo)#changes the icon of the windows acording to the phot in the windows that is created

label = Label(window,
                      text="Hello Miguel",             #adds text to the label
                      font=("Arial", 40, "bold"),  # add the font , width of letter and ttpes:bold or italic etc..
                      foreground="red",             #changes the color of the text
                      background="black",        #changes the background color of label , does not apply to the windows only label
                      relief=RAISED,                  # defines the border types
                      bd=10,                                # defines the sizes of border
                      padx=20, #width                       #defines the padding in left and right side of the label, also doesn't apply to the windows
                      pady=20, #height                      #defines the padding in top and down side of the label, also doesn't apply to the windows
                      image=resized,                  #adds the photo that is already defined in code, or already resized also
                      compound='bottom')        #defines where to put the image acording to the label

#label.pack() #defines the place to put the label , in this case it puts in middle because because of pack function
label.place(x=0, y=0) # defines the place to put the label, in this case puts in your x and y position because of place function

window.mainloop()