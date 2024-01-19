from tkinter import *
from tkinter.ttk import *
import time

def Start():
    GB = 100
    download = 0
    speed = 1
    while(download<GB):
        time.sleep(0.05)
        bar['value'] += speed
        download += speed
        percent.set(str(int(download))+"%")
        text.set(str(download)+"/100 GB completed")
        windows.update_idletasks()


windows = Tk()

percent = StringVar()
text = StringVar()

bar =Progressbar(windows,orient=HORIZONTAL,length=300)
bar.pack(pady =10)

percentlabel = Label(windows, textvariable=percent).pack()
tasklabel = Label(windows, textvariable=text).pack()

Button = Button(windows, text="Download",command=Start).pack()

windows.mainloop()