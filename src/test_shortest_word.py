"""
Tests for shortest word kata
"""
import pytest

PARAMETERS_LIST = [
    (('Lets all go on holiday somewhere very cold'), 2),
    (('i want to travel the world writing code one day'), 1),
    (('lets talk about javascript the best language'), 3),
    (('turns out random test cases are easier than writing out basic ones'), 3),
    (('bitcoin take over the world maybe who knows perhaps'), 3),
    ('', 0)
 ]

PARAMETERS_LIST_FOR_ARE_VALID_WORDS = [
    ('Lets all go on holiday somewhere very cold', True),
    ('i want to travel the world writing code one day', True),
    ('lets talk about javascript the best language', True),
    ('turns out random test cases are easier than writing out basic ones', True),
    ('bitcoin take over the world maybe who knows perhaps', True),
    ('', True),
    ([], False),
    ({}, False),
    ((), False)
]


@pytest.mark.parametrize(
    'words, result',
    PARAMETERS_LIST)
def test_find_short(words, result):
    """
    tests find_short
    """
    from shortest_word import find_short
    assert find_short(words) == result


@pytest.mark.parametrize('words, result', PARAMETERS_LIST_FOR_ARE_VALID_WORDS)
def test_are_valid_words(words, result):
    """
    test are_valid_words
    """
    from shortest_word import are_valid_words
    assert are_valid_words(words) == result
