import pytest

PARAMETERS_LIST = [
    ([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, - 2, 5], 5),
    ([20, 1, -1, 2, -2, 3, 3, 3, 5, 1, 2, 4, 20, 4, -1, - 2, 5], 3),
    ([20, 1, -1, 2, -2, 3, 3, 1, 5, 1, 2, 4, 20, 4, -1, - 2, 5], 1),
    ([20, 1, -1, 2, -2, 3, 3, 1, 5, 1, 2, 4, 20, 4, -1, - 2, 5], 1),
]


@pytest.mark.parametrize('a_collection, result', PARAMETERS_LIST)
def test_find_it(a_collection, result):
    """
    test find_it function
    """
    from find_the_odd_int import find_it
    assert find_it(a_collection) == result
