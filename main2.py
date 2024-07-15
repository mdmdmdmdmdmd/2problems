def longest_sequence_of_1s_start_position(num):
    # Convert number to binary string without the '0b' prefix
    binary_representation = bin(num)[2:]
    
    max_length = 0
    max_start_position = -1
    
    current_length = 0
    current_start_position = -1
    
    for i, char in enumerate(binary_representation):
        if char == '1':
            if current_length == 0:
                current_start_position = i + 1  # Position is 1-indexed
            current_length += 1
            if current_length > max_length:
                max_length = current_length
                max_start_position = current_start_position
        else:
            current_length = 0
    
    return max_start_position

def main():
    try:
        # Get user input
        num = int(input("Enter a number: "))
        
        # Find the starting position of the longest sequence of 1s
        result = longest_sequence_of_1s_start_position(num)
        
        # Print the result
        print(f"The starting position of the longest continuous sequence of 1s in the binary representation of {num} is: {result}")
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
