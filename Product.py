class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
        self.__amount = 0

    def getAmount(self):
        return self.__amount

    def setAmount(self, amount):
        self.__amount = amount