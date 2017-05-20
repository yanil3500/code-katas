"""
Tests for Case Reversal Of Consecutive Duplicates
"""
import pytest

PARAMETERS_LIST = [
    (('hello world'), 'heLLo world'),
    (('HELLO WORLD'), 'HEllO WORLD'),
    (('HeLlo World'), 'HeLlo World'),
    (('WWW'), 'www'),
    (('muzzles'), 'muZZles'),
    (('passive'), 'paSSive'),
    (('llama'), 'LLama'),
    (('letters are uppercase'), 'leTTers are uPPercase')
]


@pytest.mark.parametrize('words, result', PARAMETERS_LIST)
def test_reverse(words, result):
    from case_reversal_of_consecutive_duplicates import reverse_case
    assert reverse_case(words) == result
