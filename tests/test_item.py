"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src import item
import pytest


@pytest.fixture()
def class_instance():
    """Создаем пример экземпляра класса"""
    return item.Item('Планшет', 15000, 5)


def test_calculate_total_price(class_instance):
    """Проверяем рассчет общей стоимости товара"""
    assert class_instance.calculate_total_price() == 75000


def test_apply_discount(class_instance):
    """Проверяем рассчет с учетом скидки"""
    class_instance.pay_rate = 0.9
    class_instance.apply_discount()
    assert class_instance.price == 13500


def test_name_getter(class_instance):
    """Проверка геттера для name"""
    assert class_instance.name == 'Планшет'


def test_name_setter(class_instance):
    """Проверка сеттера для name"""
    class_instance.name = 'Принтер'
    assert class_instance.name == 'Принтер'
    class_instance.name = 'Преобразователь'
    assert class_instance.name == 'Преобразов'


def test_instantiate_from_csv():
    """класс-метод инициализирует экземпляры из файла csv"""
    item.Item.instantiate_from_csv()
    assert len(item.Item.all) == 5


def test_string_to_number():
    """статический метод возвращает число из числа-строки"""
    assert item.Item.string_to_number('5') == 5
    assert item.Item.string_to_number('5.0') == 5
    assert item.Item.string_to_number('5.5') == 5
