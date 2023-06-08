import pytest
import datetime


@pytest.fixture(scope='class')
def start():
    start = datetime.datetime.now()
    yield
    stop = datetime.datetime.now()
    print(f'Все тесты класса, начало: {start},'
          f'\nВсе тесты класса, окончание:: {stop}')


@pytest.fixture()
def delta_time():
    start = datetime.datetime.now()
    yield
    stop = datetime.datetime.now()
    time = stop - start
    print(f"Время выполнения теста: {time}")
