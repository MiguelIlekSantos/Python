from tkinter import *
from tkinter import messagebox
def click():
    #messagebox.showinfo(title="this is a message box info", message='You are a person')
    #messagebox.showwarning(title="Warning", message='You have a virus')
    #messagebox.showerror(title="Error", message='Something went wrong')

    if messagebox.askokcancel(title="Ask ok cancel", message='Do You want to do the thing?'):
        while True:
            messagebox.showwarning(title="Warning", message='You have a virus')
    else:
        print("You are safe")

    '''
    if messagebox.askyesno(title="ask yes or no", message="Do you like cake?"):
        print("i like cake too")
    else:
        print("Why do you not like cake?: ")
    '''
    '''
    if messagebox.askyesno(title="ask yes or no", message="Do you like cake?"):
       print("I like cake too")
    else:
        print("Why do you not like cake?: ")
    '''
    '''
    answer = messagebox.askquestion(title="Ask Question",message="Do You like pie?")
    if answer == 'yes':
        print("I like pie too!!")
    else:
        print("Why don't you like pie?")
    '''
    '''    
    answer = messagebox.askyesnocancel(title='Yes no cancel', message='Do you like coding?', icon='error')
    if answer:
        print("Then You are good person")
    elif not answer:
        print("You are mother fucker pidaras khilep")
    else:
        print("You have dogged the question!!")'''


window = Tk()

button = Button(window, text="click me", command=click)
button.pack()

window.mainloop()
