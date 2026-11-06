import tkinter as tk
from tkinter import messagebox

from ProductController import *

root = tk.Tk()
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

def makeRow(name, price, amount):
    row = root.grid_size()[1]
    row += 1
    tk.Label(root, text=name).grid(row=row, column=0)
    tk.Label(root, text=price).grid(row=row, column=1)
    tk.Label(root, text=amount).grid(row=row, column=2)

def buttonHolder():
    response = addProduct(entry1.get(), entry2.get())
    if not response:
        messagebox.showerror("Error", "Product not added")
    else:
        makeRow(entry1.get(), entry2.get(), 0)

def pageInit():
    #Titulos
    tk.Label(root, text="Product name:").grid(row=0, column=0)
    tk.Label(root, text="Price").grid(row=1, column=0)

    #Entradas
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)

    #Botão
    tk.Button(text="Create", command=buttonHolder).grid(row=2, column=1)

    #Enunciado da tabela
    tk.Label(root, text="Name").grid(row=4, column=0)
    tk.Label(root, text="Price").grid(row=4, column=1)
    tk.Label(root, text="Amount").grid(row=4, column=2)

    for product in readData():
        makeRow(product.name, product.price, product.getAmount())

    root.mainloop()


pageInit()




