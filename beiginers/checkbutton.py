import tkinter as tk

my_windo = tk.Tk()

my_windo.geometry('300x150')
my_windo.title("check the respective box for the language you want in the place ")
"""
def my_upd():
    if c7_v.get() == 1:
        c1.select()
        c2.select()
        c3.select()
        c4.select()
        c5.select()
        c6.select()
    else:
        c1.deselect()
        c2.deselect()
        c3.deselect()
        c4.deselect()
        c5.deselect()
        c6.deselect()
"""


def my_upd():
    i = 0
    if c1_v.get() == 1: i = i + 1
    if c2_v.get() == 1: i = i + 1
    if c3_v.get() == 1: i = i + 1
    if c4_v.get() == 1: i = i + 1
    if c5_v.get() == 1: i = i + 1
    if c6_v.get() == 1: i = i + 1
    if i >= 3:
        if c1_v.get() != 1: c1.config(state='disable')
        if c2_v.get() != 1: c2.config(state='disable')
        if c3_v.get() != 1: c3.config(state='disable')
        if c4_v.get() != 1: c4.config(state='disable')
        if c5_v.get() != 1: c5.config(state='disable')
        if c6_v.get() != 1: c6.config(state='disable')
    else:
        c1.config(state='normal')
        c2.config(state='normal')
        c3.config(state='normal')
        c4.config(state='normal')
        c5.config(state='normal')
        c6.config(state='normal')


c1_v = tk.IntVar(my_windo)
c1 = tk.Checkbutton(my_windo, text="python", variable=c1_v)
c1.grid(row=1, column=1)

c2_v = tk.IntVar(my_windo)
c2 = tk.Checkbutton(my_windo, text="java", variable=c2_v)
c2.grid(row=1, column=2)

c3_v = tk.IntVar(my_windo)
c3 = tk.Checkbutton(my_windo, text="javaScript", variable=c3_v)
c3.grid(row=1, column=3)

c4_v = tk.IntVar(my_windo)
c4 = tk.Checkbutton(my_windo, text="Html And css", variable=c4_v)
c4.grid(row=1, column=4)

c5_v = tk.IntVar(my_windo)
c5 = tk.Checkbutton(my_windo, text="PHP", variable=c5_v)
c5.grid(row=1, column=5)

c6_v = tk.IntVar(my_windo)
c6 = tk.Checkbutton(my_windo, text="Sql", variable=c6_v)
c6.grid(row=1, column=6)

'''c7_v = tk.IntVar(my_windo)
c7 = tk.Checkbutton(my_windo, text="status all", command=my_upd, variable=c7_v)
c7.grid(row=2, column=1)'''

my_windo.mainloop()
