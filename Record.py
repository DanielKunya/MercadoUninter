class Record:
    def __init__(self, product, user, amount, signal, date):
        self.product = product
        self.date = date
        self.user = user
        self.amount = amount
        self.signal = signal

    def toDict(self):
        return {
            "product": self.product.toDict(),
            "user": self.user,
            "date": self.date,
            "amount": self.amount,
            "signal": self.signal
        }
