import time
from random import randint
from typing import Callable


range_exp = range(1, 1_000_001)


def set_for_search():
    """Возвращает множество из миллиона чисел."""
    set_for_search = set([_ for _ in range_exp])
    return set_for_search


def list_for_search():
    """Возвращает список из миллиона чисел."""
    list_for_search = [_ for _ in range_exp]
    return list_for_search


def finder(attemps: int, number: int,  func: Callable):
    result = 0
    seq = func()
    for i in range(attemps):
        start = time.perf_counter()
        if number in seq:
            stop = time.perf_counter()
            result += stop - start
            continue
    print(
        f"Число {number} найдено {attemps} раз "
        f"в последовательности {type(seq)} за {result:.5f} сек."
    )
    return result


def test_set_speed() -> None:
    """Тест для сравнения скорости поиска по вхождению.

    Между списком и множеством из миллиона чисел.
    """
    # rand_num = randint(1, 1_000_001)
    rand_num = 300

    set_speed = finder(10000, rand_num,  set_for_search)

    list_speed = finder(10000, rand_num, list_for_search)

    faster_var = min(set_speed, list_speed)
    longest_var = max(set_speed, list_speed)

    print(f"Разница в {longest_var/faster_var:.0f} раз!!!")
