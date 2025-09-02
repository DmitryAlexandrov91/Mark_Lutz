import pytest
import time


@pytest.fixture
def timer():
    return time.perf_counter


@pytest.fixture
def fabric(timer):
    """Фабрика, производяшая REPS вычислений функцией func из NUM."""
    def factory(func, reps, num):
        def wrapper():
            start = timer()
            for _ in range(reps):
                func(num)
            end = timer()
            print(
                f"Функция {func.__name__} произвела {reps:_}"
                f" операций над числом {num}"
                f" за {end - start:.5f} сек"
            )
        return wrapper
    return factory


@pytest.fixture
def random_user_data(faker):
    """Случайный словарь с данными юзера."""
    return {
        'first_name': faker.first_name(),
        'last_name': faker.last_name(),
        'email': faker.email(),
        'address': faker.address()
    }
