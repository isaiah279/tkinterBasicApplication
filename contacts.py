"""contacts = ["kenya",
            "uganda",
            "Tanazania",
            "Egypy",
            "Somalia",
            "Nigerial,"
            "Sychels",
            "Sudan"]
for i in contacts:
    print(i)

import turtle"""

"""import turtle as arb

import time
def myFun():
    colors=["red","blue","green","yellow","orange","brown"]
    t=arb
    t.pensize(5)
    t.bgcolor("black")
    t.speed(1000)
    for x in range(360):
        t.pencolor(colors[x%len(colors)])
        t.pensize(x/50)
        t.forward(x)
        t.left(590000)
myFun()
time.sleep(5)"""
import mysql.connector
from mysql.connector import connection
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Inventory System")
root.geometry("1080x720")

storeName = "BimBAAAA SariSari Store"

host = "localhost"
dbuser = "renzy"
password = "code"
dbname = "inventory"


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Database Connection Established")
    except:
        print("Error Connecting from Database")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Success query")
    except:
        print("Error query")


def insert_data():
    itemId = str(entryId.get())
    itemName = str(entryName.get())
    itemPrice = str(entryPrice.get())
    itemQuantity = str(entryQuantity.get())
    if itemId == "" or itemName == " ":
        print("Error Inserting Id")
    if itemName == "" or itemName == " ":
        print("Error Inserting Name")
    if itemPrice == "" or itemPrice == " ":
        print("Error Inserting Price")
    if itemQuantity == "" or itemQuantity == " ":
        print("Error Inserting Quantity")
    else:
        entryId.delete(0, END)
        entryName.delete(0, END)
        entryPrice.delete(0, END)
        entryQuantity.delete(0, END)
        execute_query(
            connection,
            "INSERT INTO itemsinfo " +
            "(item_id,item_name,item_price,item_quantity) " +
            "VALUES " +
            "('" + itemId + "','" + itemName + "','" + itemPrice + "','" + itemQuantity + "')"
        )

    for i in my_tree.get_children():
        my_tree.delete(i)

    results = read_data(connection, "SELECT * FROM itemsinfo")

    for result in results:
        my_tree.insert(parent='', index='end', iid=0, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)


def delete_data():
    selected_item = my_tree.selection()[0]
    delete = str(my_tree.item(selected_item)['values'][0])
    execute_query(
        connection,
        "DELETE FROM itemsinfo WHERE item_id = '" + delete + "'")

    for i in my_tree.get_children():
        my_tree.delete(i)

    results = read_data(connection, "SELECT * FROM itemsinfo")

    for result in results:
        my_tree.insert(parent='', index='end', iid=0, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)


def read_data(connection, query):
    global cursor
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print("Read Data Success")
        return result
    except:
        print("Error read data")


connection = create_connection(host, dbuser, password, dbname)

titleLabel = Label(root, text=storeName, font=('Arial bold', 30), bd=2)
titleLabel.grid(row=0, column=0, columnspan=8, padx=20, pady=20)

idLabel = Label(root, text="ID", font=('Arial bold', 15))
nameLabel = Label(root, text="Name", font=('Arial bold', 15))
priceLabel = Label(root, text="Price", font=('Arial bold', 15))
quantityLabel = Label(root, text="Quantity", font=('Arial bold', 15))
idLabel.grid(row=1, column=0, padx=10, pady=10)
nameLabel.grid(row=2, column=0, padx=10, pady=10)
priceLabel.grid(row=3, column=0, padx=10, pady=10)
quantityLabel.grid(row=4, column=0, padx=10, pady=10)

entryId = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryName = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryPrice = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryQuantity = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryId.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
entryName.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
entryPrice.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
entryQuantity.grid(row=4, column=1, columnspan=3, padx=5, pady=5)

buttonEnter = Button(
    root, text="Enter", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#0099ff", command=insert_data)
buttonEnter.grid(row=5, column=1, columnspan=1)

buttonUpdate = Button(
    root, text="Update", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#ffff00")
buttonUpdate.grid(row=5, column=2, columnspan=1)

buttonDelete = Button(
    root, text="Delete", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#e62e00", command=delete_data)
buttonDelete.grid(row=5, column=3, columnspan=1)

my_tree = ttk.Treeview(root)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial bold', 15))

my_tree['columns'] = ("ID", "Name", "Price", "Quantity")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=W, width=100)
my_tree.column("Name", anchor=W, width=200)
my_tree.column("Price", anchor=W, width=150)
my_tree.column("Quantity", anchor=W, width=150)
my_tree.heading("ID", text="ID", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Price", text="Price", anchor=W)
my_tree.heading("Quantity", text="Quantity", anchor=W)

for i in my_tree.get_children():
    my_tree.delete(i)

results = read_data(connection, "SELECT * FROM itemsinfo")

for result in results:
    my_tree.insert(parent='', index='end', iid=0, text="", values=(result), tag="orow")

my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 15))
my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

root.mainloop()