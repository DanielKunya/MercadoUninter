from random import randrange
from Product import Product
import json
from fileManagment import readData, writeData

def searchProduct(search=False):
    #Caso a busca seja com id
    if type(search)==int:
        for product in stock:
            if product.id == search:
                return product

    #Caso a busca seja com nome
    elif type(search)==str:
        for product in stock:
            if product.name == search:
                return product

    #O dado não foi identificado
    else:
        print("No entry ever typed")
        return False
    print("Product not found")

    #Busca não encontrada
    return False

def addProduct(name, price):
    global stock
    stock = readData()
    duplicate = False

    #Checagem por duplicatas
    for product in stock:
        if product.name.lower() == name.lower():
            duplicate = True

    if duplicate == False:
        id = len(stock)
        print(stock)
        if id == 0:
            id = 0
        else:
            id = stock[-1].id + 1

        product = Product(id, name, price)
        stock.append(product)

        writeData(stock)
        stock = readData()
        return True
    else:
        return False


def removeProduct(id):
    global stock
    stock = readData()

    stock.data.remove(searchProduct(id))

    writeData(stock)
    stock = readData()

def manageStock(search, amount):
    global stock
    stock = readData()

    product = searchProduct(search)
    productAmount = product.getAmount()

    if product != False:
        if productAmount + amount < 0:
            product.setAmount(0)
            print(f"O valor extrapola em {productAmount + amount}")
        else:
            product.setAmount(productAmount + amount)

    writeData(stock)
    stock = readData()