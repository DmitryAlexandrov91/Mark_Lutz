import pytest

from src.part_4.exerscises.ex_9 import (get_sqert_gen_expr,  # noqa
                                        get_sqrt_for_cycle,
                                        get_sqrt_list_compr, get_sqrt_map)


@pytest.fixture
def seq():
    return [2, 4, 9, 16, 25]


@pytest.fixture
def seq_sqrt():
    return [1.4142135623730951, 2.0, 3.0, 4.0, 5.0]


def test_cycle(seq, seq_sqrt):
    result = get_sqrt_for_cycle(seq)
    assert result == seq_sqrt


def test_sqrt_map(seq, seq_sqrt):
    result = get_sqrt_map(seq)
    assert result == seq_sqrt


def test_sqrt_list_compr(seq, seq_sqrt):
    result = get_sqrt_list_compr(seq)
    assert result == seq_sqrt


def test_sqrt_gen_expr(seq, seq_sqrt):
    result = get_sqert_gen_expr(seq)

    assert result is iter(result)
    assert list(result) == seq_sqrt
