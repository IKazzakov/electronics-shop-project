class InstantiateCSVError(Exception):
    """
    Класс-исключение
    если файл `item.csv` поврежден (например, отсутствует одна из колонок данных)
    """
    def __init__(self, *args):
        self.message = args[0] if args else 'Файл item.csv поврежден'

    def __str__(self):
        return f'{self.message}'
