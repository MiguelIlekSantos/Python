from tkinter import *
#text widget = function like a text area , you can enter multiple lines of text

def submit():
    answer = text.get('1.0',END)
    print(answer)

window = Tk()

text = Text(window,
                    foreground='blue',
                    font=("Sans serif",20),
                    height=8,
                    width=20,
                    padx=20,
                    pady=20)
text.pack()

button = Button(window, text='Submit',command=submit)
button.pack()

window.mainloop()