"""Тестирование функций квадратного корня."""
from src.part_4.exerscises.ex_10 import sqrt_math, sqrt_pack, sqrt_pow


def test_same_result(faker):
    """Все функции квадратного корня возвращают один результат."""
    random_int = faker.random_int()

    assert sqrt_pow(
        random_int
    ) == sqrt_math(random_int) == sqrt_pack(random_int)


def test_sqrt_math(fabric):
    fabric(sqrt_math, 10_000_000, 100)()


def test_sqrt_pack(fabric):
    fabric(sqrt_pack, 10_000_000, 100)()


def test_sqrt_pow(fabric):
    fabric(sqrt_pow, 10_000_000, 100)()
