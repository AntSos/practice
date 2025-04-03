"""
Improve Caesar Cipher

-Allow the shifted value to come from the range 1..25 inclusive.
-Let the code preserve the letters' case (lower-case letters will remain lower-case) and all non-alphabetical characters should remain untouched.

"""


# Main function
def main():
    message: str = input("Enter your message: ")

    # Check if s_value is a number using a while loop
    while True:
        s_value: str = input("Enter a renage between 1 to 25: ")
        # Try to change s_value to an integer
        try:
            s_value_n: int = int(s_value)
            # If it is a valid number between 1 to 25 break
            if s_value_n > 0 and s_value_n <= 25:
                break
        # If it is not an integer, print message and keep in the loop
        except:
            print("You must enter an integer between 1 to 25!")

    # Call encode function
    result: str = encode(message, s_value_n)
    print(result)


def encode(message: str, range: int) -> str:
    """A function to encode the message according to the range"""
    # Empty string
    l_encode: str = ""
    # Loop through every letter in the message
    for character in message:
        # Ask if the letter is lower according to its ASCII code
        if ord(character) >= 97 and ord(character) <= 122:
            # If the sum of the ASCII code + range is greater than 122, add ASCII number code + range, then subtract 122, and finally add 96
            if (ord(character) + range) > 122:
                character = chr(((ord(character) + range) - (122)) + 96)
                l_encode += character
            # Any other case, add ASCII number code + range
            else:
                character = chr(ord(character) + range)
                l_encode += character
            # Ask if the letter is upper according to its ASCII code
        elif ord(character) >= 65 and ord(character) <= 90:
            # If the sum of the ASCII code + range is greater than 90, add ASCII number code + range, then subtract 90, and finally add 64
            if (ord(character) + range) > 90:
                character = chr(((ord(character) + range) - (90)) + 64)
                l_encode += character
            # Any other case, add ASCII number code + range
            else:
                character = chr(ord(character) + range)
                l_encode += character

        # If is any other character, add it
        else:
            l_encode += character
    # Return the l_encode string as a str using .join()
    return l_encode


if __name__ == "__main__":
    main()
