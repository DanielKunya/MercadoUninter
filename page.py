import tkinter
import tkinter as tk
from asyncio.tools import build_task_table
from itertools import product
from tkinter import messagebox

from Product import Product
from ProductController import *


# Programa principal
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Product Management System")
        self.geometry("600x400")

        # Criação das páginas
        self.tela1 = Login(self)
        self.stockMenu = StockMenu(self)

        # Execução da primera página
        self.stockMenu.pack()

    # Função para troca de Páginas
    def showPage(self, showScreen, hideScreen):
        hideScreen.pack_forget()
        showScreen.pack()


# Tela de Login
class Login(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Input de nome
        tk.Label(self, text="Enter your name").pack()
        entry1 = tk.Entry(self)
        entry1.pack()

        # Botão de entrar
        tk.Button(self, command=lambda: master.showPage(master.stockMenu, self), text="Enter").pack()


# Menu de estoque
class StockMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Cabeçário da Página
        tk.Label(self, text="Stock Menu").grid(row=0, column=1)

        # Criação dos inputs com títulos
        tk.Label(self, text="Name").grid(row=1, column=0)
        tk.Label(self, text="Price").grid(row=1, column=1)
        tk.Label(self, text="Amount").grid(row=1, column=2)
        entry1 = tk.Entry(self)
        entry2 = tk.Entry(self)
        entry3 = tk.Entry(self)
        entry1.grid(row=2, column=0)
        entry2.grid(row=2, column=1)
        entry3.grid(row=2, column=2)

        # Botão para executar criação
        tk.Button(self, text="Create", command=lambda: self.createRow(entry1.get(), entry2.get(), entry3.get())).grid(
            row=3, column=1)

        # Lista dos produtos na sua forma Label
        self.stockLabelList = []
        self.updateList()

    # Atualiza a lista do estoque
    def updateList(self):

        # Destroi todos os elementos de estoque atuais
        for label in self.stockLabelList:
            label.destroy()
        self.stockLabelList.clear()

        # Cria os elemntos Label de estoque
        for index, product in enumerate(readData(), start=4):
            name = tk.Label(self, text=product.name)
            price = tk.Label(self, text=product.price)
            amount = tk.Label(self, text=product.getAmount())

            name.grid(row=index, column=0)
            price.grid(row=index, column=1)
            amount.grid(row=index, column=2)

            name.bind("<Button-1>", lambda e, p=product: EditModal(self, p))
            price.bind("<Button-1>", lambda e, p=product: EditModal(self, p))
            amount.bind("<Button-1>", lambda e, p=product: editAmountModal(self, p))

            self.stockLabelList.extend([name, price, amount])

    #Função responsável por atualizar a lsita visível, deve ser cahamada em qualquer alteração
    def createRow(self, name, price, amount):
        response = addProduct(name, price)
        if response:
            self.updateList()
        else:
            messagebox.showerror("Error", "Product not added")

#Janela para edição do produto
class EditModal(tk.Toplevel):
    def __init__(self, master, product):
        super().__init__(master)
        self.title("Edit Product")
        self.pid = product.id

        #Criação dos Labels
        tk.Label(self, text=f"Editing {product.name}").grid(row=0, column=0, columnspan=2)
        tk.Label(self, text="Name: ").grid(row=1, column=0)
        tk.Label(self, text="Price: ").grid(row=2, column=0)
        tk.Label(self, text="Amount: ").grid(row=3, column=0)

        # Criação dos inputs
        self.entry1 = tk.Entry(self)
        self.entry2 = tk.Entry(self)
        self.entry1.grid(row=1, column=1)
        self.entry2.grid(row=2, column=1)

        # Inicia a caixa de texto com o valor do produto chamado
        self.entry1.insert(0, product.name)
        self.entry2.insert(0, product.price)

        #Botão de salvar
        tk.Button(self, text="Save", command=lambda: self.saveHandle()).grid(row=3, column=0, columnspan=2)

        #Certifica de que a Janela está visível, e mantém como primeiro plano
        self.wait_visibility()
        self.grab_set()

    #Função para assegurar a interação com o botão de Salvar
    def saveHandle(self):
        response = editProduct(self.pid, self.entry1.get(), self.entry2.get())

        if response:
            self.master.updateList()
            self.destroy()
        else:
            messagebox.showerror("Error", "Product not edited")

# Janela de alteração da quantidade do produto
class editAmountModal(tk.Toplevel):
    def __init__(self, master, product):
        super().__init__(master)
        self.title("Edit Amount")
        self.pid = product.id

        # Criação dos Labels informativos
        tk.Label(self, text="    ").grid(row=0, column=0, columnspan=2)
        tk.Label(self, text=f"Product {product.name}").grid(row=1, column=0, columnspan=2)
        tk.Label(self, text=f"Amount: {product.getAmount()}").grid(row=2, column=0, columnspan=2)

        # Rodinha de valor
        self.entry1 = tk.Spinbox(self, increment=1, from_=0, to=1000)
        self.entry1.grid(row=3, column=0, columnspan=2)

        # Botões de adicionar e remover
        tk.Button(self, text="Remove", command=lambda: self.saveHandle(self.entry1.get(), False)).grid(row=4, column=0)
        tk.Button(self, text="Add", command=lambda: self.saveHandle(self.entry1.get(), True)).grid(row=4, column=1)

        #Certifica que a tela carregou e põe prioridade
        self.wait_visibility()
        self.grab_set()

    #Interação com o botão de adicionar e remvoer
    def saveHandle(self, value, signal):
        value = int(value)
        
        if signal == False:
            value = value * -1

        response = manageStock(self.pid, value)

        if response:
            self.master.updateList()
            self.destroy()
        else:
            messagebox.showerror("Error", "Product not edited")


app = App()
app.mainloop()
