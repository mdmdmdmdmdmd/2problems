# src/main.py

import re

def split_and_remove_punctuation(statement):
    # Use regex to replace punctuation with spaces
    statement = re.sub(r'[^\w\s]', ' ', statement)
    # Split into words
    words = statement.split()
    return words

def find_word_with_most_chars(statement, char):
    words = split_and_remove_punctuation(statement)
    max_count = 0
    max_word = ""

    for word in words:
        count = word.count(char)
        if (count > max_count) or (count == max_count and len(word) > len(max_word)):
            max_count = count
            max_word = word
        elif count == max_count and len(word) == len(max_word):
            if statement.index(max_word) > statement.index(word):
                max_word = word

    if max_count>0:
        return max_word


