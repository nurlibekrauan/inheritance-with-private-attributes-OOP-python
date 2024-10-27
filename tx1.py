from datetime import datetime


class Product:
    def __init__(self, name, price, quantity, cost_price, arrival_date):
        self.set_name(name)
        self.set_price(price)
        self.set_quantity(quantity)
        self.set_cost_price(cost_price)
        self.set_arrival_date(arrival_date)

    # Сеттеры с проверками
    def set_name(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Название товара должно быть непустой строкой.")
        self.name = name

    def set_price(self, price):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Цена должна быть положительным числом.")
        self.price = price

    def set_quantity(self, quantity):
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Количество должно быть неотрицательным целым числом.")
        self.quantity = quantity

    def set_cost_price(self, cost_price):
        if not isinstance(cost_price, (int, float)) or cost_price < 0:
            raise ValueError("Себестоимость должна быть положительным числом.")
        self.__cost_price = cost_price

    def get_cost_price(self):
        return self.__cost_price

    def set_arrival_date(self, arrival_date):
        try:
            # Преобразование строки в объект даты
            self.__arrival_date = datetime.strptime(arrival_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                "Дата поступления на склад должна быть в формате YYYY-MM-DD."
            )

    def get_arrival_date(self):
        return self.__arrival_date


class Electronics(Product):
    def __init__(self, name, price, quantity, cost_price, arrival_date, warranty_type):
        super().__init__(name, price, quantity, cost_price, arrival_date)
        self.set_warranty_type(warranty_type)

    def set_warranty_type(self, warranty_type):
        if not isinstance(warranty_type, int) or warranty_type < 0:
            raise ValueError(
                "Гарантия должна быть положительным целым числом (в годах)."
            )
        self.__warranty_type = warranty_type

    def get_warranty_years(self):
        return self.__warranty_type


class Clothing(Product):
    def __init__(self, name, price, quantity, cost_price, arrival_date, material):
        super().__init__(name, price, quantity, cost_price, arrival_date)
        self.set_material(material)

    def set_material(self, material):
        if not isinstance(material, str) or not material.strip():
            raise ValueError("Материал должен быть непустой строкой.")
        self.__material = material

    def get_material(self):
        return self.__material


class Food(Product):
    def __init__(self, name, price, quantity, cost_price, arrival_date, expiry_date):
        super().__init__(name, price, quantity, cost_price, arrival_date)
        self.set_expiry_date(expiry_date)

    def set_expiry_date(self, expiry_date):
        try:
            # Преобразование строки в объект даты
            self.__expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Срок годности должен быть в формате YYYY-MM-DD.")

    def get_expiry_date(self):
        return self.__expiry_date


# Пример использования с проверками:
try:
    tv = Electronics(
        name="Smart TV",
        price=500,
        quantity=10,
        cost_price=400,
        arrival_date="2024-09-12",
        warranty_type=2,
    )
    shirt = Clothing(
        name="Shirt",
        price=50,
        quantity=100,
        cost_price=30,
        arrival_date="2024-09-12",
        material="Cotton",
    )
    apple = Food(
        name="Apple",
        price=1,
        quantity=500,
        cost_price=0.5,
        arrival_date="2024-09-12",
        expiry_date="2024-12-01",
    )
    print("Все товары успешно созданы.")
except ValueError as e:
    print(f"Ошибка при создании товара: {e}")
