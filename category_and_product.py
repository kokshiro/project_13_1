class Category:

    name = str
    description = str
    product = list

    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = set()
        Category.total_categories += 1
    def add_product(self, product):
        self.__products.add(product)

        Category.total_unique_products = len(self.__products)

    @property
    def products(self):
        product_info = []
        for product in self.__products:
            info = f'{product.name}, {product.price} руб. Остаток: {product.count_in_stock} шт.'
            product_info.append(info)
        return "\n".join(product_info)




class Product:
    name = str
    description = str
    price = float
    count_in_stock = int

    def __init__(self, name, description, price, count_in_stock):
        self.name = name
        self.description = description
        self.__price = float(price)
        self.count_in_stock = int(count_in_stock)

    @classmethod
    def create_product(cls, name, description, price, count_in_stock):
        return cls(name, description, price, count_in_stock)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена введена некорректно")
        else:
            self.__price = value

one_1 = Category("Electronics", "Electronic devices")
two_2 = Product("Laptop", "High-performance laptop", 1500, 4)
two_3 = Product("Mouse", "Wireless mouse", 30.00, 20)
two_4 = Product("Laptop", "High-performance laptop", 1500, 4)
one_1.add_product(two_2)
one_1.add_product(two_3)
one_1.add_product(two_4)

print(one_1.products)

# Проверка сеттера price
two_2.price = 1700.0  # Изменение цены на корректное значение
print(f"Новая цена для {two_2.name}: {two_2.price}")

two_2.price = -5.0  # Попытка установить некорректное значение цены
print(f"Новая цена для {two_2.name}: {two_2.price}")

