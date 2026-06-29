from tranliterator import *

def test_simple_word_from_cyrillic_to_latin():
    text = "Салам"
    assert cyrillic_to_latin(text) == "Salam"

def test_simple_word_from_latin_to_cyrillic():
    text = "Salam"
    assert latin_to_cyrillic(text) == "Салам"

def test_retransliteration():
    text = "Salam"
    text = latin_to_cyrillic(text)
    text = cyrillic_to_latin(text)

    assert text == "Salam"


    