# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


class Test:

    def test_round(self, start):
        assert all_division(4, 1) == 4.0

    def test_one(self, start):
        assert all_division(0, 1) == 0.0

    def test_round_zero(self, start):
        assert all_division(-5, 5) == -1.0

    def test_three(self, start, delta_time):
        assert all_division(1, -5) == -0.2

    def test_zero(self, start):
        assert all_division(10, 1) == 10
