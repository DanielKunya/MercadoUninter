from Product import Product
import json

from Record import Record
from fileManagment import readData, writeData, readHistory


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

        writeData(data=stock)
        stock = readData()
        return True
    else:
        return False


def removeProduct(id):
    global stock
    stock = readData()

    stock.data.remove(searchProduct(id))

    writeData(data=stock)
    stock = readData()

def manageStock(search, amount, date, user):
    global stock
    global history
    history = readHistory()
    stock = readData()

    product = searchProduct(search)
    productAmount = product.getAmount()
    signal = ""

    if amount > 0:
        signal = True
    elif amount < 0:
        signal = False


    if product != False:
        if productAmount + amount < 0:
            return False
        else:
            product.setAmount(productAmount + amount)

    record = Record(product, user, amount, signal, date)
    history.append(record)

    writeData(data=stock, history=history)
    stock = readData()
    return True

def editProduct(id, nname, nprice):
    global stock
    stock = readData()
    product = searchProduct(id)

    if product == False:
        return False
    else:
        product.name = nname
        product.price = nprice
        writeData(data=stock)
        stock = readData()
        return True

