import tkinter as tk

my_window = tk.Tk()
my_window.geometry('300x100')

my_str = tk.StringVar(my_window)  # DECLARING A VARIABLE TO THE WINDOW

e1 = tk.Entry(my_window, bg="yellow", textvariable=my_str, font=20)  # ENTRIES IN THE COLUMNS
e1.grid(row=1, column=1, pady=20, padx=10, ipadx=50, ipady=10)

b1 = tk.Label(my_window, text="", font=("times", 10, "bold"), bd=2)

b1 = tk.Button(my_window, text="submit", font=18, state="disable")  # BUTTON OF THE ENTRY
b1.grid(row=1, column=3, ipadx=10)


def my_update(*args):
    if len(my_str.get()) > 4:
        b1.config(state="normal")
    else:
        b1.config(state="disable")


my_str.trace('w', my_update)

my_window.mainloop()
import matplotlib
