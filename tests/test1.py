# tests/test1.py

import pytest
from src.main1 import split_and_remove_punctuation, find_word_with_most_chars

def test_split_and_remove_punctuation():
    assert split_and_remove_punctuation("Hello, world!") == ["Hello", "world"]
    assert split_and_remove_punctuation("It's a test-case.") == ["It's", "a", "test-case"]
    assert split_and_remove_punctuation("") == []
    assert split_and_remove_punctuation("No punctuation here") == ["No", "punctuation", "here"]

def test_find_word_with_most_chars():
    assert find_word_with_most_chars("This is a test statement", 't') == "statement"
    assert find_word_with_most_chars("Another test case", 'e') == "Another"
    assert find_word_with_most_chars("Equal count test", 't') == "test"
    assert find_word_with_most_chars("No match here", 'z') == None
    assert find_word_with_most_chars("It's a tie", 't') == "It's"

if __name__ == "__main__":
    pytest.main()
