from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("my frame work")

def open():
    import credentialsAudio

def conv():
    protecting = data.get() ** 2
    messagebox.showinfo("the point is here", str(protecting))


frame1 = Frame(window, width=1000, height=500, highlightbackground='red', highlightthicknes=3)
frame1.grid(row=0, column=0, padx=100, pady=100, ipady=20, ipadx=20)

data= IntVar()


l1 = Label(frame1, text="Enter age :", fg="blue", font=(16)).grid(row=0, column=0, padx=100, pady=100)
text_box = Entry(frame1, fg='green',textvariable=data, font=(16)).grid(row=0, column=1)
button1 = Button(frame1, text="converter", fg='blue', command=conv, font=(16)).grid(row=1, column=1)
button2= Button(frame1, text="open", fg='blue', command=open, font=(16)).grid(row=2, column=1)


window.mainloop()
