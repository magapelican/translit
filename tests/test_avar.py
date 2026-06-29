from tranliterator import *
from tests.CASES_AVAR import *

import pytest

@pytest.mark.parametrize(
        "text, expected",
        CASES_FROM_CYRILLIC_TO_LATIN
)
def test_simple_word_from_cyrillic_to_latin(text, expected):
    assert cyrillic_to_latin(text) == expected

@pytest.mark.parametrize(
        "text, expected",
        CASES_FROM_LATIN_TO_CYRILLIC
)
def test_simple_word_from_latin_to_cyrillic(text, expected):
    assert latin_to_cyrillic(text) == expected

@pytest.mark.parametrize(
        "text",
        CASES_LATIN
)
def test_retransliteration(text):
    latin_text = latin_to_cyrillic(text)
    final_text = cyrillic_to_latin(latin_text)

    assert final_text == text


    