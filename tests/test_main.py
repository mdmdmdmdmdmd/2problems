import random
import string
import re
import time

def generate_random_character():
    # Define the character sets
    upper_letters = string.ascii_uppercase  # 1 parts
    lower_letters = string.ascii_lowercase  # 6 part
    spaces = ' '  # 2 parts
    punctuations = ",.?'\";"  # 1 part
    
    # Create a weighted list based on the ratio
    characters = upper_letters * 1 + lower_letters * 6 + spaces * 2 + punctuations * 1
    
    return random.choice(characters)

def generate_random_word(length):
    return ''.join(generate_random_character() for _ in range(length))

def generate_random_statement(word_lengths):
    words = [generate_random_word(length) for length in word_lengths]
    return ' '.join(words)

# Example usage
word_lengths = [random.randint(3, 10) for _ in range(10)]  # Generate 10 words with lengths between 3 and 10

random_statement = generate_random_statement(word_lengths)
print(f"Random Statement: {random_statement}")

# Measure elapsed time
start_time = time.time()

char='k'
find_word_with_most_chars(random_statement, char)

end_time = time.time()

elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.9f} seconds")

