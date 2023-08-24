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
