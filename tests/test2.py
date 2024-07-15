import pytest
from src.main2 import longest_sequence_of_1s_start_position

def test_positive_number():
    assert longest_sequence_of_1s_start_position(156) == 4
    assert longest_sequence_of_1s_start_position(88) == 3

def test_zero():
    assert longest_sequence_of_1s_start_position(0) == 0, "Test case for 0 failed"

def test_all_ones():
    assert longest_sequence_of_1s_start_position(7) == 1, "Test case for 7 (111) failed"
    assert longest_sequence_of_1s_start_position(15) == 1, "Test case for 15 (1111) failed"

def test_multiple_sequences():
    assert longest_sequence_of_1s_start_position(75) == 6, "Test case for 75 (1001011) failed"
    assert longest_sequence_of_1s_start_position(29) == 1, "Test case for 29 (11101) failed"
    assert longest_sequence_of_1s_start_position(219) == 1, "Test case for 219 (11011011) failed"
    assert longest_sequence_of_1s_start_position(375) == 3, "Test case for 375 (101110111) failed"

def test_negative_number():
    assert longest_sequence_of_1s_start_position(-7) == 1, "Test case for -7 (111) failed"
    assert longest_sequence_of_1s_start_position(-15) == 1, "Test case for -15 (1111) failed"

def test_single_character():
    assert longest_sequence_of_1s_start_position(1) == 1, "Test case for 1 (1) failed"
    assert longest_sequence_of_1s_start_position(2) == 1, "Test case for 2 (10) failed"

if __name__ == "__main__":
    pytest.main()
