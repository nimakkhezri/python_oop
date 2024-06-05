class SalesHistory:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def display_orders(self):
        for order in self.orders:
            print(f"سفارش شماره {order.date}:")
            print(f"  مشتری: {order.customer.get_full_name()}")
            print(f"  محصولات:")
            for product in order.products:
                print(f"    - {product['product'].get_name()}: {product['quantity']}")
            print(f"  قیمت کل: {order.get_total_price()}")
            print(f"  قیمت نهایی: {order.get_offer_price()}")
            print(f"  تاریخ: {order.date}")
            print("-" * 20)

    def display_orders_list(self):
        for i, order in enumerate(self.orders):
            print(f"{i + 1}. {order.date} - {order.customer.get_full_name()} - {order.get_offer_price()}")

    def view_order_details(self, choice):
        if 0 < choice <= len(self.orders):
            order = self.orders[choice - 1]
            print(f"سفارش شماره {order.date}:")
            print(f"  مشتری: {order.customer.get_full_name()}")
            print(f"  محصولات:")
            for product in order.products:
              print(f"    - {product['product'].get_name()}: {product['quantity']}")
            print(f"  قیمت کل: {order.get_total_price()}")
            print(f"  تخفیف: {order.discount}%")
            print(f"  قیمت نهایی: {order.get_offer_price()}")
            print(f"  تاریخ: {order.date}")
        else:
            print("شماره سفارش نامعتبر است!")

    def get_total_sales(self, start_date, end_date):
        total_sales = 0
        for order in self.orders:
            if start_date <= order.date <= end_date:
                total_sales += order.get_offer_price()
        return total_sales

    def get_orders(self):
        return self.orders

    def set_orders(self, saved_orders):
        self.orders = saved_orders
