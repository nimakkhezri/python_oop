class Order:
    def __init__(self, products, discount, customer, date):
        self.products = products
        self.discount = discount
        self.total_price = 0
        self.offer_price = 0
        self.customer = customer
        self.date = date
        self.calculate_total_price()
        self.calculate_offer_price()

    def add_product(self, product, quantity):
        if product.get_stock() >= quantity:
            self.products.append({'product': product, 'quantity': quantity})
            product.set_stock(product.get_stock() - quantity)
            self.calculate_total_price()
        else:
            print(f"There is not enough stock of product {product.get_name()}!")

    def get_offer_price(self):
        self.calculate_offer_price()
        return self.offer_price

    def get_total_price(self):
        return self.total_price

    def apply_discount(self, discount_percent):
        self.discount = discount_percent
        self.calculate_offer_price()

    def get_customer_info(self):
        return self.customer

    def calculate_total_price(self):
        self.total_price = sum(
            product['product'].get_price() * product['quantity'] for product in self.products)

    def calculate_offer_price(self):
        self.offer_price = self.total_price * (1 - self.discount / 100)