# tests/test1.py

import pytest
from src.main1 import split_and_remove_punctuation, find_word_with_most_chars

def test_split_and_remove_punctuation1():
    assert split_and_remove_punctuation("Hello, world!") == ["Hello", "world"]
def test_split_and_remove_punctuation2():
    assert split_and_remove_punctuation("It's a test-case.") == ["It's", "a", "test-case"]
def test_split_and_remove_punctuation3():
    assert split_and_remove_punctuation("") == []
def test_split_and_remove_punctuation4():
    assert split_and_remove_punctuation("No punctuation here") == ["No", "punctuation", "here"]

def test_find_word_with_most_chars1():
    assert find_word_with_most_chars("This is a test statement", 't') == "statement"
def test_find_word_with_most_chars2():
    assert find_word_with_most_chars("Another test case", 'e') == "Another"
def test_find_word_with_most_chars3():
    assert find_word_with_most_chars("Equal count test", 't') == "test"
def test_find_word_with_most_chars4():
    assert find_word_with_most_chars("No match here", 'z') == None
def test_find_word_with_most_chars5(): 
    assert find_word_with_most_chars("It's a tie", 't') == "It's"

if __name__ == "__main__":
    pytest.main()
