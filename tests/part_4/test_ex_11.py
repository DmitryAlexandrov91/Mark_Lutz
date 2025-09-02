import pytest

from src.part_4.exerscises.ex_11 import countdown


@pytest.fixture
def expected():
    return "5 4 3 2 1 stop"


def test_countdown_func(expected):
    result = countdown(5)
    assert result == expected


def test_coutdown_exp(expected):
    result = ''.join(
        [f"{number} " if number != 0 else "stop" for number in range(5, -1, -1)]
    )
    assert result == expected


def test_countdpwn_gen(expected):
    gen = (
        f"{number} " if number != 0 else "stop" for number in range(5, -1, -1)
    )
    assert gen is iter(gen)

    result = ''.join(gen)
    assert result == expected
