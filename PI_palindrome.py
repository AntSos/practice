"""
PI Palindrome LAB

-Asks the user for some text.
-Checks whether the entered text is a palindrome, and prints result.
-Assume that an empty string isn't a palindrome.
-Treat upper- and lower-case letters as equal.
-Spaces are not taken into account during the check - treat them as non-existent

"""


# Main function
def main():
    # Request the input from the user
    input_words: str = input("Write some words or numbers: ")
    # Print and call the palindrome function
    result = palindrome(input_words)
    print(result)


def palindrome(words: str) -> None:
    """A simple function to check if a text is a palindrome"""
    # Ask if the string is empty
    if words == "":
        print(f"Not palindrome, empty sting: {words}")
    else:
        # Get rid of spaces
        string_01 = words.replace(" ", "")
        # Change every letter to lower case
        string_02 = string_01.lower()
        # Ask if the reverse string is the same as the regular
        if string_02[::-1] == string_02:
            print(f"Palindrome: {words}")
        else:
            print(f"Not palindrome: {words}")


if __name__ == "__main__":
    main()