from src.part_4.exerscises.ex_5 import copyDict


def test_copy_dict() -> None:
    test_dict = {x: x for x in range(5)}
    copy_test_dict = copyDict(test_dict)

    assert test_dict == copy_test_dict
    assert test_dict is not copy_test_dict
