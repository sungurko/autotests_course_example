# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('a, b, result', [
    pytest.param(4, 1, 4.0, marks=pytest.mark.smoke),
    (0, 1, 0.0), (-5, 5, -1.0), (1, -5, -0.2),
    pytest.param(10, 0, 0, marks=pytest.mark.skip('Иногда можно делить но 0'))])
def test_division(a, b, result):
    assert all_division(a, b) == result

