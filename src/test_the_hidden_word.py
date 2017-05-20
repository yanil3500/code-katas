"""
Tests for counting duplicates
"""
import pytest

PARAMETERS_LIST = [
    (637, "aid"),
    (7415, "debt"),
    (49632, "email"),
    (942547, "melted"),

]


@pytest.mark.parametrize('text, result', PARAMETERS_LIST)
def test_hidden(text, result):
    """
    test hidden function
    """
    from the_hidden_word import hidden
    assert hidden(text) == result

