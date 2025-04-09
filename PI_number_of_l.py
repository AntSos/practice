"""
PI Number of life LAB

-asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY)
-outputs the Digit of Life for the date.

"""


def main():

    # Use a while loop to request the date
    while True:
        # Birthday user input
        bd_date: str = input(
            "Enter your birthday, only digits without symbols or spaces: "
        )
        # Check if the input is a number
        try:
            n_bd_date: int = int(bd_date)
            if n_bd_date > 100000:
                break
        except:
            print("There is something wrong with your input, try again!")

    # Using sum_str function
    f_d_life: int = sum_str(bd_date)
    if f_d_life < 10:
        print(f"Your digit of life is: {f_d_life}")
    else:
        # Transform the number to a str
        str_f_d_life: str = str(f_d_life)
        # Using sum_str function
        final_d_o_l: int = sum_str(str_f_d_life)
        print(f"Your digit of life is: {final_d_o_l}")

def sum_str(num_str: str) -> int:
    """This function receives a string of integers and returns its sum as an integer"""
    # Transform the str to a list
    l_num_str: list[str] = list(num_str)
    # Transform every character of the previous list to an integer
    n_l_num_str: list[str] = [int(character) for character in l_num_str]
    # Sum the elements of the previous list
    f_number: int = sum(n_l_num_str)
    return f_number

if __name__ == "__main__":
    main()
