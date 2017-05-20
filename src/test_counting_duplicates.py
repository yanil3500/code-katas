"""
Tests for counting duplicates
"""
import pytest

PARAMETERS_LIST = [
    ("abcde", 0),
    ("abcdea", 1),
    ("indivisibility", 1),
    ("aabbcdeB", 2),
    ("aa11", 2),
    ("bbbb890011", 3),
    ("mmonnettt", 3),
    ("Pack my box with five dozen liquor jugs", 4),
    ("the quick brown fox jumped over the lazy dog", 7),
    ("Jerry Jackdaws love my big sphinx of quartz.", 8)
]


@pytest.mark.parametrize('text, result', PARAMETERS_LIST)
def test_duplicate_count(text, result):
    """
    test counting_duplicates function
    """
    from counting_duplicates import duplicate_count
    assert duplicate_count(text) == result