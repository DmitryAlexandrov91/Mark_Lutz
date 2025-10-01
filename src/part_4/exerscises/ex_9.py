from math import sqrt

test_list = [2, 4, 9, 16, 25]


def get_sqrt_for_cycle(seq):
    res = []
    for x in seq:
        res.append(sqrt(x))
    return res


def get_sqrt_map(seq):
    return list(map(sqrt, seq))


def get_sqrt_list_compr(seq):
    return [sqrt(x) for x in seq]


def get_sqert_gen_expr(seq):
    for x in seq:
        yield sqrt(x)
