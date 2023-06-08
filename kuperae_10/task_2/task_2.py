# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_round():
    assert all_division(4, 1) == 4.0


def test_one():
    assert all_division(0, 1) == 0.0


def test_round_zero():
    assert all_division(-5, 5) == -1.0


@pytest.mark.smoke
def test_three():
    assert all_division(1, -5) == -0.2


def test_zero():
    assert all_division(10, 0) == 0, 'Нельзя делить на ноль'
