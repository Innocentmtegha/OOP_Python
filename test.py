class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        print(f"An item is created: {name}, Price: {price}, Quantity: {quantity}")

    def calculate_total_price(self, x, y):
        return x * y


item1 = Item("Phone", 100, 5)
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item("Laptop", 1000, 3)
print(item2.calculate_total_price(item2.price, item2.quantity))

item3 = Item("Tablet", 500, 2)
print(item3.calculate_total_price(item3.price, item3.quantity))
