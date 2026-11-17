import os
import json

from Record import Record
from Product import Product

DATABASE = "database.json"


def readData():
    # Se o arquivo não existe, ele cria
    if not os.path.exists(DATABASE):
        startData = {"data": [], "history": []}

        with open(DATABASE, "w", encoding="utf-8") as file:
            json.dump(startData, file)

        return []

    # Abre o arquivo e "converte" para json
    with open(DATABASE, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Transforma em uma lista
    stock = []
    for item in data.get("data"):
        product = Product(item["id"], item["name"], item["price"])
        product.setAmount(item["amount"])
        stock.append(product)

    return stock


def readHistory():
    # Se o arquivo não existe, ele cria
    if not os.path.exists(DATABASE):
        startData = {"data": [], "history": []}

        with open(DATABASE, "w", encoding="utf-8") as file:
            json.dump(startData, file)

        return []

    with open(DATABASE, "r", encoding="utf-8") as file:
        data = json.load(file)

    history = []
    for item in data.get("history"):
        product = Product(item["product"]["id"], item["product"]["name"], item["product"]["price"])
        product.setAmount(item["product"]["amount"])

        record = Record(product, item["user"], item["amount"], item["signal"], item["date"])
        history.append(record)

    return history


def writeData(data=False, history=False):
    convertedData = {"data": [], "history": []}

    if data != False and history == False:
        oldHist = readHistory()
        convertedData = {
            "data": [product.toDict() for product in data],
            "history": [record.toDict() for record in oldHist]
        }
    elif history != False and data == False:
        oldDat = readData()
        convertedData = {
            "data": [product.toDict() for product in oldDat],
            "history": [record.toDict() for record in history]
        }
    else:
        convertedData = {
            "data": [product.toDict() for product in data],
            "history": [record.toDict() for record in history]
        }

    # Abre o arquivo em modo de escrita
    with open(DATABASE, "w", encoding="utf-8") as file:
        json.dump(convertedData, file, indent=4)
