from src import keyboard
import pytest


@pytest.fixture()
def keyboard_instance():
    """Создаем пример экземпляра класса"""
    return keyboard.Keyboard('Dark Project KD87A', 9600, 5)


def test_change_lang(keyboard_instance):
    """Тесты для проверки переключения раскладки клавиатуры"""
    assert str(keyboard_instance.language) == "EN"
    keyboard_instance.change_lang()
    assert str(keyboard_instance.language) == "RU"
    # Сделали EN -> RU -> EN
    keyboard_instance.change_lang()
    assert str(keyboard_instance.language) == "EN"

    with pytest.raises(AttributeError) as excpt:
        keyboard_instance.language = 'CH'
    assert str(excpt.value) == "can't set attribute 'language'"
