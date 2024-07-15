# Coding Problems Repository

## Description
This repository contains the solution to the 2 coding problems assigned by JPMC. It includes the source code, unit test cases/results, and explanations.


## How to Install

To install the dependencies, run the following command:

```bash
pip install -r required_libs.txt
```

## How to Run the Code
```bash
python src/main1.py
python src/main2.py
```

## How to Run Tests
```bash
# Ensure the pytest package is installed. If not, run the following command:
# pip install pytest
pytest -v tests/test1.py
pytest -v tests/test2.py
```



## Explanation of the Solution

## Logic
Explain the logic behind your solution here.

## Assumptions & Edge Case Scenarios
Provide an analysis of the time and space complexity of your solution.

## Unit Testing Results

[Problem 1]

split_and_remove_punctuation("Hello, world!") => **["Hello", "world"]**  
split_and_remove_punctuation("It's a test-case.") => **["It's", "a", "test-case"]**  
split_and_remove_punctuation("") => **[]**  
split_and_remove_punctuation("No punctuation here") => **["No", "punctuation", "here"]**  

find_word_with_most_chars("This is a test statement", 't') => **"statement"**  
find_word_with_most_chars("Another test case", 'e') => **"Another"**  
find_word_with_most_chars("Equal count test", 't') => **"test"**  
find_word_with_most_chars("No match here", 'z') => **None**  
find_word_with_most_chars("It's a tie", 't') => **"It's"**  
find_word_with_most_chars("An apple", 'A') => **"An"**
