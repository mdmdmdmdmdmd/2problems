# src/main.py

import re

def split_and_remove_punctuation(statement):
    # Use regex to replace punctuation with spaces
    # Keep hyphens (-) and apostrophes (') as they are typically part of words
    statement = re.sub(r"[^\w\s'-]", ' ', statement)
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
    return None


def main():
    # Get user input for the statement and the character
    statement = input("Enter a statement: ")
    char = input("\nEnter a character to search for: ")
    
    if len(char) != 1:
        print("Please enter a single character.")
        return

    result = find_word_with_most_chars(statement, char)
     
    # ANSI escape code for bold text
    bold_start = "\033[1m"
    bold_end = "\033[0m"
        
    if result:       
        print(f"\n\nThe word with the most occurrences of '{char}' is: {bold_start}{result}{bold_end}")
    else:
        print(f"\n\nNo word contains the character {bold_start}'{char}'{bold_end}.")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
