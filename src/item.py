import csv
import os.path
from src.csv_errors import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    CSV_PATH = os.path.join('..', 'src', 'items.csv')  # Путь к файлу .csv

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        """отображение информации об объекте класса в режиме отладки """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """отображение информации об объекте класса для пользователей"""
        return self.name

    def __add__(self, other):
        """
        Сложение двух экземпляров класса по значению количество товаров.
        Проверка принадлежности экземпляров к классу Item ил дочернему
        """
        if not isinstance(other, Item):
            raise ValueError("Складывать можно только объекты класса Item и дочерних от него")
        else:
            return self.quantity + other.quantity

    @property
    def name(self):
        """Геттер для атрибута name"""
        return self.__name

    @name.setter
    def name(self, name):
        """Сеттер для name, с проверкой длины наименования товара"""
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        """Класс-метод, инициализирующий экземпляры класса `Item`
        данными из файла _src/items.csv"""
        try:
            with open(cls.CSV_PATH, encoding='cp1251') as csvfile:
                reader = csv.DictReader(csvfile)
                if reader.fieldnames != ['name', 'price', 'quantity']:
                    raise InstantiateCSVError
                cls.all.clear()
                for row in reader:
                    if any(value is None for value in row.values()):
                        raise InstantiateCSVError
                    cls(row['name'], float(row['price']), int(row['quantity']))
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(string):
        """статический метод, возвращающий число из числа-строки"""
        return int(float(string))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
