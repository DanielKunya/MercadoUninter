from random import randrange

from Product import Product

stock = []

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
    id = len(stock)
    if id == 0:
        id = 0
    else:
        id = stock[-1].id + 1

    product = Product(id, name, price)
    stock.append(product)

def removeProduct(id):
    stock.remove(searchProduct(id))

def manageStock(search, amount):
    product = searchProduct(search)
    productAmount = product.getAmount()

    if product != False:
        if productAmount + amount < 0:
            product.setAmount(0)
            print(f"O valor extrapola em {productAmount + amount}")
        else:
            product.setAmount(productAmount + amount)

addProduct("Parafuso", 3.00)
addProduct("Porca", 2.00)
addProduct("Prego", 1.00)
removeProduct(1)
addProduct("Roldana", 5.00)
print(searchProduct(3).name)
print(searchProduct("Roldana").price)

for product in stock:
    manageStock(product.id, randrange(0,10))
    manageStock(product.id, (randrange(0,5) * -1))
    print([product.id, product.name, product.price, product.getAmount()])
