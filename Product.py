class Product:
    def __init__(self, name, stock, price):
        self.name = name
        self.stock = stock
        self.price = price

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_stock(self):
        return self.stock

    def set_stock(self, stock):
        self.stock = stock

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price