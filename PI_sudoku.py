"""
Python Institute LAB: Sudoku

-> Reads 9 rows of the Sudoku, each containing 9 digits.
-> Outputs Yes if the Sudoku is valid, and No otherwise.
"""

# Matrix that will contain the sudoku numbers
s_matrix: list[str] = []

def main():
    # Counter for each row
    count: int = 1
    # While loop for an organized input
    while len(s_matrix) < 9:
        row = input(f'Enter nine integers between 1 to 9 for the row {count}: ')
        c_row = check_input(row)

        if c_row == False:
            print('Enter only nine integers from 1 to 9')
        # Else: append count += 1 and append c_row to s_matrix
        else:
            count += 1
            s_matrix.append(c_row)
            #break

    # Check and assign a result in every element of the matrix in a dictionary using check_numbers function 
    result: dict = {'row_01': check_numbers(s_matrix[0]),
                    'row_02': check_numbers(s_matrix[1]),
                    'row_03': check_numbers(s_matrix[2]),
                    'row_04': check_numbers(s_matrix[3]),
                    'row_05': check_numbers(s_matrix[4]),
                    'row_06': check_numbers(s_matrix[5]),
                    'row_07': check_numbers(s_matrix[6]),
                    'row_08': check_numbers(s_matrix[7]),
                    'row_09': check_numbers(s_matrix[8]),
                    }
    
    for k, v in result.items():
        print(k, v)

    

def check_input(row: list[str]) -> list[int] | bool:
    """Checks if the input values are valid"""
    # Try to conver it each value to an integer
    try:
        # List to store the int values
        c_row = [int(e) for e in row]
        
    # Except return False        
    except: 
        return False

    # Check if the length is 9
    if len(c_row) != 9:
        return False
    # Check if 0 is in the row 
    if 0 in c_row:
        return False
    # Return only 9 integers    
    return c_row

def check_numbers(numbers_list: list[int]) -> bool:
    """Counts and checks if the values in a list are only one time"""
    # Initialize a dictionary to count each value in the list
    counts: dict = {}
    # For every number in the given list
    for num in numbers_list:
        # counts dictionary key[num] = key[num] + 1, using get() method
        counts[num] = counts.get(num, 0) + 1
    # Check every value from the dictionary
    for value in counts.values():
        # If one of them is different from 1, return false
        if value != 1:
            return False
    # Otherwise, return true
    return True

if __name__=='__main__':
    main()