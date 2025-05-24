"""
Python Institute LAB: Sudoku
Create a program that:
-> Reads 9 rows of the Sudoku, each containing 9 digits.
-> Outputs Yes if the Sudoku is valid, and No otherwise.
"""


def main():
    # While loop for an organized input
    while True:
        sudoku = input(f"Enter in one line, 81 integers between 1 to 9 : ")
        c_matrix = check_input(sudoku)

        if c_matrix == False:
            print("Enter only 81 integers from 1 to 9")
        # Else: break the loop
        else:
            break

    # Check and assign a result in every element of the matrix in a dictionary using check_numbers function
    result: dict = {
        "row_01": check_sudoku(c_matrix[0:9]),
        "row_02": check_sudoku(c_matrix[9:18]),
        "row_03": check_sudoku(c_matrix[18:27]),
        "row_04": check_sudoku(c_matrix[27:36]),
        "row_05": check_sudoku(c_matrix[36:45]),
        "row_06": check_sudoku(c_matrix[45:54]),
        "row_07": check_sudoku(c_matrix[54:63]),
        "row_08": check_sudoku(c_matrix[63:72]),
        "row_09": check_sudoku(c_matrix[72:81]),
        "column_01": check_sudoku(
            [
                c_matrix[0],
                c_matrix[9],
                c_matrix[18],
                c_matrix[27],
                c_matrix[36],
                c_matrix[45],
                c_matrix[54],
                c_matrix[63],
                c_matrix[72],
            ]
        ),
        "column_02": check_sudoku(
            [
                c_matrix[1],
                c_matrix[10],
                c_matrix[19],
                c_matrix[28],
                c_matrix[37],
                c_matrix[46],
                c_matrix[55],
                c_matrix[64],
                c_matrix[73],
            ]
        ),
        "column_03": check_sudoku(
            [
                c_matrix[2],
                c_matrix[11],
                c_matrix[20],
                c_matrix[29],
                c_matrix[38],
                c_matrix[47],
                c_matrix[56],
                c_matrix[65],
                c_matrix[74],
            ]
        ),
        "column_04": check_sudoku(
            [
                c_matrix[3],
                c_matrix[12],
                c_matrix[21],
                c_matrix[30],
                c_matrix[39],
                c_matrix[48],
                c_matrix[57],
                c_matrix[66],
                c_matrix[75],
            ]
        ),
        "column_05": check_sudoku(
            [
                c_matrix[4],
                c_matrix[13],
                c_matrix[22],
                c_matrix[31],
                c_matrix[40],
                c_matrix[49],
                c_matrix[58],
                c_matrix[67],
                c_matrix[76],
            ]
        ),
        "column_06": check_sudoku(
            [
                c_matrix[5],
                c_matrix[14],
                c_matrix[23],
                c_matrix[32],
                c_matrix[41],
                c_matrix[50],
                c_matrix[59],
                c_matrix[68],
                c_matrix[77],
            ]
        ),
        "column_07": check_sudoku(
            [
                c_matrix[6],
                c_matrix[15],
                c_matrix[24],
                c_matrix[33],
                c_matrix[42],
                c_matrix[51],
                c_matrix[60],
                c_matrix[69],
                c_matrix[78],
            ]
        ),
        "column_08": check_sudoku(
            [
                c_matrix[7],
                c_matrix[16],
                c_matrix[25],
                c_matrix[34],
                c_matrix[43],
                c_matrix[52],
                c_matrix[61],
                c_matrix[70],
                c_matrix[79],
            ]
        ),
        "column_09": check_sudoku(
            [
                c_matrix[8],
                c_matrix[17],
                c_matrix[26],
                c_matrix[35],
                c_matrix[44],
                c_matrix[53],
                c_matrix[62],
                c_matrix[71],
                c_matrix[80],
            ]
        ),
        "square_01": check_sudoku(
            [
                c_matrix[0],
                c_matrix[1],
                c_matrix[2],
                c_matrix[9],
                c_matrix[10],
                c_matrix[11],
                c_matrix[18],
                c_matrix[19],
                c_matrix[20],
            ]
        ),
        "square_02": check_sudoku(
            [
                c_matrix[3],
                c_matrix[4],
                c_matrix[5],
                c_matrix[12],
                c_matrix[13],
                c_matrix[14],
                c_matrix[21],
                c_matrix[22],
                c_matrix[23],
            ]
        ),
        "square_03": check_sudoku(
            [
                c_matrix[6],
                c_matrix[7],
                c_matrix[8],
                c_matrix[15],
                c_matrix[16],
                c_matrix[17],
                c_matrix[24],
                c_matrix[25],
                c_matrix[26],
            ]
        ),
        "square_04": check_sudoku(
            [
                c_matrix[27],
                c_matrix[28],
                c_matrix[29],
                c_matrix[36],
                c_matrix[37],
                c_matrix[38],
                c_matrix[45],
                c_matrix[46],
                c_matrix[47],
            ]
        ),
        "square_05": check_sudoku(
            [
                c_matrix[30],
                c_matrix[31],
                c_matrix[32],
                c_matrix[39],
                c_matrix[40],
                c_matrix[41],
                c_matrix[48],
                c_matrix[49],
                c_matrix[50],
            ]
        ),
        "square_06": check_sudoku(
            [
                c_matrix[33],
                c_matrix[34],
                c_matrix[35],
                c_matrix[42],
                c_matrix[43],
                c_matrix[44],
                c_matrix[51],
                c_matrix[52],
                c_matrix[53],
            ]
        ),
        "square_07": check_sudoku(
            [
                c_matrix[54],
                c_matrix[55],
                c_matrix[56],
                c_matrix[63],
                c_matrix[64],
                c_matrix[65],
                c_matrix[72],
                c_matrix[73],
                c_matrix[74],
            ]
        ),
        "square_08": check_sudoku(
            [
                c_matrix[57],
                c_matrix[58],
                c_matrix[59],
                c_matrix[66],
                c_matrix[67],
                c_matrix[68],
                c_matrix[75],
                c_matrix[76],
                c_matrix[77],
            ]
        ),
        "square_09": check_sudoku(
            [
                c_matrix[60],
                c_matrix[61],
                c_matrix[62],
                c_matrix[69],
                c_matrix[70],
                c_matrix[71],
                c_matrix[78],
                c_matrix[79],
                c_matrix[80],
            ]
        ),
    }
    # Store the values that are False acording to check_sudoku function
    wrong_sudoku_parts: list[bool] = []
    # Loop throgh each key, value in the dictionary results
    for key, value in result.items():
        # If a value is equal to False, store it in wrong_sudoku_parts list
        if value == False:
            wrong_sudoku_parts.append(key)
        else:
            continue

    # Check if an element of the dictionary result is False
    if False in result.values():
        print(f"No Sudoku Square!, check{wrong_sudoku_parts}")
    else:
        print("Yes Sudoku Square!")


def check_input(user_input: list[str]) -> list[int] | bool:
    """Checks if the input values are valid"""
    # Get rid of sapaces and line jumps
    sudoku_matrix = user_input.replace(" ", "").replace("/n", "")
    # Try to conver it each value to an integer
    try:
        # List to store the int values
        sudoku_matrix = [int(e) for e in user_input]

    # Except return False
    except:
        return False

    # Check if the length is 81
    if len(sudoku_matrix) != 81:
        return False
    # Check if 0 is in the matrix
    if 0 in sudoku_matrix:
        return False
    # Return only 81 integers
    return sudoku_matrix


def check_sudoku(numbers_list: list[int]) -> bool:
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


if __name__ == "__main__":
    main()
