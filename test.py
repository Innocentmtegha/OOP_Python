class Item:
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


print(Item.is_integer(5))  # True
print(Item.is_integer(5.0))  # True
print(Item.is_integer(5.5))  # False
