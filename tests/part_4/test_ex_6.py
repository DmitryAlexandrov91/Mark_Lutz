from src.part_4.exerscises.ex_6 import addDict


def test_add_dict_for_dict(faker) -> None:
    dict_1 = {
        'first_name': faker.first_name(),
        'last_name': faker.last_name(),
    }

    dict_2 = {
        'email': faker.email(),
        'address': faker.address(),
        'last_name': faker.last_name(),
    }

    new_dict = addDict(obj_1=dict_1, obj_2=dict_2)

    assert isinstance(new_dict, dict)
    for key in dict_1.keys():
        assert key in new_dict.keys()
    for key in dict_2.keys():
        assert key in new_dict.keys()


def test_add_dict_for_list() -> None:
    none_list = None
    list_1 = [1, 2, 3]
    list_2 = [4, 5, 6]
    new_list = addDict(none_list, list_2)
    assert isinstance(new_list, list)
    assert new_list == list_2
    new_list = addDict(list_1, list_2)
    assert isinstance(new_list, list)
    for x in list_1:
        assert x in new_list
    for x in list_2:
        assert x in new_list
