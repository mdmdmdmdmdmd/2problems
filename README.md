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
### [Problem 1] `src/main1.py` 
---
## Logic

### Function: `split_and_remove_punctuation`
      Remove Punctuation => Split Statement into Words => Return the List of Words
      
      - The function uses a regular expression to replace all characters that are not word 
            characters (`\w`), whitespace (`\s`), hyphens (`-`), or apostrophes (`'`) with a space.
            
      - This preserves hyphens and apostrophes as they are often part of words (e.g., "it's", "test-case").
   
### Function: `find_word_with_most_chars`
      Split the Statement => Initialize Counters => Iterate Through Words => Return Result
   
### Function: `main`
      Get User Input => Validate Input => Find Word with Most Occurrences of the Character => Print Result

## Assumptions

**- Hyphens (`-`) and apostrophes (`'`) are considered part of words and are not removed.**<br>
**- The input character for `find_word_with_most_chars` should be a single character.**<br>
**- The function treats words case-sensitively when counting character occurrences.**

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

   ("This is a test statement", 't')  =>  **"statement"**  
   ("Another test case", 'e')  =>  **"Another"**  
   ("Equal count test", 't')  =>  **"test"**  
   ("No match here", 'z')  =>  **None**  
   ("It's a tie", 't')  =>  **"It's"**  
   ("An apple", 'A')  =>  **"An"**

---
<br><br>



### [Problem 2] `src/main2.py` 
---
## Logic

### Function: `longest_sequence_of_1s_start_position`
      Convert Number to Binary => Initialize Variables => Iterate Through Binary Representation => Return Result

### Function: `main`
      Get User Input => Find the Starting Position => Print the Result => Handle Invalid Input

## Assumptions

**-Input is an Integer**:
   - The function assumes that the input is an integer (positive, negative, or zero).

**-Binary Representation Handling for Negative Numbers**:
   - For negative numbers, the binary representation excludes the sign bit (i.e., the first three characters are handled).

**-Position is 1-Indexed**:
   - The function returns the starting position of the longest continuous sequence of 1s as a 1-indexed value, meaning the first position is 1.

## Edge Cases

1. **Input is 0**:
   - When the input is 0, the binary representation is `0`. There are no 1s, so the function should return 0.

2. **No 1s in Binary Representation**:
   - If the binary representation of the number does not contain any 1s (e.g., numbers like 0), the function should handle this gracefully.

3. **All 1s in Binary Representation**:
   - If the binary representation of the number is all 1s (e.g., numbers like 7 which is `111` in binary), the function should correctly identify the entire string as the longest sequence.

4. **Multiple Sequences of 1s**:
   - If there are multiple sequences of 1s of the same maximum length, the function should return the starting position of the first such sequence.

5. **Single Long Sequence in the Middle**:
   - If the longest sequence of 1s is surrounded by 0s on both sides (e.g., `0011100`), the function should still correctly identify the starting position of this sequence.

6. **Single Character Input**:
   - If the binary representation is a single character (either `0` or `1`), the function should handle it correctly.

7. **Negative Numbers**:
   - The function correctly handles negative numbers by ignoring the sign bit and considering the two's complement representation.




## Unit Testing Results


