from tkinter import *
from tkinter import ttk
from tkinter import messagebox

ws = Tk()
ws.title('Python guides')
ws.geometry("1200x1000")
ws.config(bg='#fb0')
tree_view = ttk.Treeview(ws)
tree_view['columns'] = ('Rank', 'Name', 'Badget')
tree_view.column('#0', width=0, stretch=NO)
tree_view.column('Rank', anchor=CENTER, width=200)
tree_view.column('Name', anchor=CENTER, width=200)
tree_view.column('Badget', anchor=CENTER, width=200)

tree_view.heading("#0", text='', anchor=E)
tree_view.heading("Rank", text="Id", anchor=CENTER)
tree_view.heading('Name', text='rank', anchor=CENTER)
tree_view.heading('Badget', text='Badget', anchor=CENTER)

tree_view.insert(parent='', index=0, iid=0, text='')
tree_view.insert(parent='', index=1, iid=1, text='')
tree_view.insert(parent='', index=2, iid=2, text='')
tree_view.insert(parent='', index=3, values=('4'))
tree_view.insert(parent='', index=4)
tree_view.pack()


tree=ttk.Treeview
ws.mainloop()
