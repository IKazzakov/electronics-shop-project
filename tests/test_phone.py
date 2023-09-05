from src import phone
import pytest


@pytest.fixture()
def phone_instance():
    """Создаем пример экземпляра класса"""
    return phone.Phone("iPhone 14", 120_000, 5, 2)


def test_repr(phone_instance):
    """тест для repr"""
    assert repr(phone_instance) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(phone_instance):
    """тест для str"""
    assert str(phone_instance) == 'iPhone 14'


def test_verify_num_of_sim(phone_instance):
    """тест для проверки ввода некорректных значений"""
    with pytest.raises(ValueError) as excpt:
        phone_instance.number_of_sim = 0
    assert str(excpt.value) == 'Количество физических SIM-карт должно быть целым числом больше нуля.'
    phone_instance.number_of_sim = 1
    assert phone_instance.number_of_sim == 1



