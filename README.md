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



## Explanation of the Solutions

### [Problem 1] `src/main1.py` Explanation

## Logic

### Function: `split_and_remove_punctuation`

```mermaid
flowchart TD
    A[Start] --> B[Get user input for statement and character]
    B --> C{Is the character input length 1?}
    C -->|No| D[Print error message and return]
    C -->|Yes| E[Call split_and_remove_punctuation(statement)]
    E --> F[Initialize max_count to 0 and max_word to ""]
    F --> G[Iterate through words]
    G --> H{count > max_count or (count == max_count and length(word) > length(max_word))}
    H -->|Yes| I[Update max_count and max_word]
    H -->|No| J{count == max_count and length(word) == length(max_word)}
    J -->|Yes| K{index of max_word > index of word}
    K -->|Yes| I
    K -->|No| L
    J -->|No| L[Continue iteration]
    L --> G
    G --> M{max_count > 0}
    M -->|Yes| N[Return max_word]
    M -->|No| O[Return None]
    N --> P[Print the word with the most occurrences of the character in bold]
    O --> Q[Print message indicating no word contains the character]
    P --> R[End]
    Q --> R[End]

2. **Remove Punctuation**:
   - The function uses a regular expression to replace all characters that are not word characters (`\w`), whitespace (`\s`), hyphens (`-`), or apostrophes (`'`) with a space.
   - This preserves hyphens and apostrophes as they are often part of words (e.g., "it's", "test-case").

3. **Split Statement into Words**:


4. **Return the List of Words**:


### Function: `find_word_with_most_chars`

1. **Split the Statement**:
   - The function first calls `split_and_remove_punctuation` to get a list of words from the statement.

2. **Initialize Counters**:
   - `max_count` is initialized to 0 to keep track of the maximum number of occurrences of the character.
   - `max_word` is initialized to an empty string to store the word with the most occurrences of the character.

3. **Iterate Through Words**:
   - For each word, the function counts the occurrences of the specified character using the `count()` method.
   - If the count is greater than `max_count`, or if the count is equal to `max_count` but the word is longer than `max_word`, the function updates `max_count` and `max_word`.
   - If the count and length are the same, the function checks the index of the current `max_word` and the current word in the statement. If the current word appears earlier, it updates `max_word`.

4. **Return Result**:
   - If `max_count` is greater than 0, the function returns `max_word`.
   - Otherwise, it returns `None`.

### Function: `main`

1. **Get User Input**:
   - The function prompts the user to enter a statement and a character.

2. **Validate Input**:
   - If the length of the character input is not 1, the function prints an error message and returns.

3. **Find Word with Most Occurrences of the Character**:
   - The function calls `find_word_with_most_chars` with the user's inputs.

4. **Print Result**:
   - If a word is found, it prints the word in bold using ANSI escape codes.
   - If no word is found, it prints a message indicating that no word contains the character.

## Assumptions

- Hyphens (`-`) and apostrophes (`'`) are considered part of words and are not removed.
- The input character for `find_word_with_most_chars` should be a single character.
- The function treats words case-sensitively when counting character occurrences.

## Edge Cases

1. **Empty Statement**:
   - If the input statement is empty, `split_and_remove_punctuation` returns an empty list, and `find_word_with_most_chars` returns `None`.

2. **No Matching Characters**:
   - If no word contains the specified character, `find_word_with_most_chars` returns `None`.

3. **Multiple Words with Same Character Count**:
   - If multiple words have the same highest count of the specified character, the function returns the longest word.
   - If there are words of the same length, it returns the first one in the statement.

4. **Special Characters**:
   - All characters except word characters, whitespace, hyphens, and apostrophes are replaced with spaces.
   - This includes punctuation marks, special symbols, and numbers.

5. **Case Sensitivity**:
   - The function counts character occurrences in a case-sensitive manner. For example, 'A' and 'a' are considered different characters.

By following the above logic and considering the assumptions and edge cases, the functions are designed to handle a variety of input scenarios effectively.


## Unit Testing Results

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
