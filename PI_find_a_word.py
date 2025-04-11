"""
PI Find a word! Lab

-answers the following question: are the characters comprising the first string hidden inside the second string?.
-you should use the two-argument variants of the find() function.
-don't worry about case sensitivity.
"""


def main():
    # Request a word and then the text
    word: str = input("Enter a word to look for: ").lower()
    text: str = input("Enter the the text: ").lower()
    # This variable will allow the same string as the word given, if this is present in the text
    final_str: str = ""
    # Stores the position where to begin and continue looking with the find method
    position: int = 0
    # loop through every character in the word given
    for character in word:
        # result variable will store if the find method finds the character inside the text, from the position to the len of the text
        result = text.find(character, position, len(text))
        # If the variable result finds the character (is this greater than -1)
        if result > -1:
            # The position´s value will be changed to the index of the character, using the result variable
            position = result
            # The character will be added to final_str
            final_str += character
        # If not, continue
        else:
            continue
    # Compare both strings and print the requested result
    if word == final_str:
        print("Yes!")
    else:
        print("No!")


if __name__ == "__main__":
    main()
