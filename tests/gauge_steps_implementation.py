import re
from getgauge.python import step, data_store

def split_and_remove_punctuation(statement):
    statement = re.sub(r"[^\w\s'-]", ' ', statement)
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

    if max_count > 0:
        return max_word
    return None

@step("Given the input <statement>")
def given_input_statement(statement):
    data_store.spec['statement'] = statement

@step("The words should be <expected_words>")
def verify_split_and_remove_punctuation(expected_words):
    statement = data_store.spec['statement']
    expected_words = expected_words.split(',')
    actual_words = split_and_remove_punctuation(statement)
    assert actual_words == expected_words, f"Expected {expected_words}, but got {actual_words}"

@step("Given the input <statement> and character <char>")
def given_input_statement_and_character(statement, char):
    data_store.spec['statement'] = statement
    data_store.spec['char'] = char

@step("The result should be <expected_word>")
def verify_find_word_with_most_chars(expected_word):
    statement = data_store.spec['statement']
    char = data_store.spec['char']
    actual_word = find_word_with_most_chars(statement, char)
    assert actual_word == expected_word, f"Expected {expected_word}, but got {actual_word}"
