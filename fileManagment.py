import os
import json

from Product import Product

DATABASE = "database.json"

def readData():
    #Se o arquivo não existe, ele cria
    if not os.path.exists(DATABASE):
        startData = {"data":[]}

        with open(DATABASE, "w", encoding="utf-8") as file:
            json.dump(startData, file)

        return []

    #Abre o arquivo e "converte" para json
    with open(DATABASE, "r", encoding="utf-8") as file:
        data = json.load(file)

    #Transforma em uma lista
    stock = []
    for item in data.get("data"):
        product = Product(item["id"], item["name"], item["price"])
        product.setAmount(item["amount"])
        stock.append(product)

    return stock

def writeData(data):

    convertedData = {
        "data": [product.toDict() for product in data]
    }

    #Abre o arquivo em modo de escrita
    with open(DATABASE, "w", encoding="utf-8") as file:
        json.dump(convertedData, file, indent=4)