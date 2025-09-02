from mark_lutz.part_4.exerscises.ex_12 import recursion_factorial, reduce_factorial, cycle_factorial, math_factorial  # noqa


def test_recursion_fact(fabric):
    assert recursion_factorial(1) == 1
    assert recursion_factorial(2) == 2
    assert recursion_factorial(3) == 6
    assert recursion_factorial(6) == 720
    fabric(recursion_factorial, 100000, 100)()


def test_reduce_factorial(fabric):
    assert reduce_factorial(1) == 1
    assert reduce_factorial(2) == 2
    assert reduce_factorial(3) == 6
    assert reduce_factorial(6) == 720
    fabric(reduce_factorial, 100000, 100)()


def test_cycle_factorial(fabric):
    assert cycle_factorial(1) == 1
    assert cycle_factorial(2) == 2
    assert cycle_factorial(3) == 6
    assert cycle_factorial(6) == 720
    fabric(cycle_factorial, 100000, 100)()


def test_math_factorial(fabric):
    assert math_factorial(1) == 1
    assert math_factorial(2) == 2
    assert math_factorial(3) == 6
    assert math_factorial(6) == 720
    fabric(math_factorial, 100000, 100)()
