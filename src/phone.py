from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса item. param name, price, quantity подтягиваются из родительского класса Item.
        :param number_of_sim: Количество сим карт.
        """
        super().__init__(name, price, quantity)
        self.verify_num_of_sim(number_of_sim)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """отображение информации об объекте класса в режиме отладки """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @classmethod
    def verify_num_of_sim(cls, number):
        """проверка правильности ввода количества сим карт"""
        if type(number) != int or number <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    @property
    def number_of_sim(self):
        """геттер для количества сим карт"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        """сеттер для количетсва сим карт с проверкой правильности ввода"""
        self.verify_num_of_sim(number)
        self.__number_of_sim = number
