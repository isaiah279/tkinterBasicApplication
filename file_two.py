import tkinter as tk
from tkinter import *

root = tk.Tk()
tk.Label(root, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
'''number_chosen=tk.Entry(root,width=12,textvariable=number,state='readonly')
number_chosen=(1,2,3,4,5,6,74)
number_chosen.grab_current(0)
'''
root.geometry("900x500")

chVarDis = tk.IntVar()

check1 = tk.Checkbutton(root, text="Disable", textvariable=chVarDis, state='disabled')
check1.select()
check1.grid(row=4, column=0, sticky=tk.W)

chVarUn = tk.IntVar()

check2 = tk.Checkbutton(root, text="Unchecked", textvariable=chVarDis)

check2.grid(row=4, column=2, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(root, text="Enabled", textvariable=chVarDis, font="34")

check3.grid(row=4, column=3, sticky=tk.W)

#radiobutton globals
COLOR1="Blue"
COLOR2="Green"
COLOR3="Gold"

def radCall():
    radSel=radVar.get()
    if radSel==1:root.config(bg=COLOR1)
    elif radSel==2:root.config(bg=COLOR2)
    elif radSel==3:root.config(bg=COLOR3)




radVar=tk.IntVar()
rL=tk.Label(root,text=COLOR1).grid(row=6,column=1)
rad1=tk.Radiobutton(root,textvariable=radVar,command=radCall)
rad1.grid(row=6,column=2,columnspan=1,sticky=tk.W)

rL2=tk.Label(root,text=COLOR2).grid(row=6,column=3)
rad2=tk.Radiobutton(root,textvariable=radVar,command=radCall)
rad2.grid(row=6,column=5,columnspan=2,sticky=tk.W)

rL3=tk.Label(root,text=COLOR3).grid(row=6,column=6)
rad3=tk.Radiobutton(root,textvariable=radVar,command=radCall)
rad3.grid(row=6,column=8,columnspan=3,sticky=tk.W)

root.mainloop()
