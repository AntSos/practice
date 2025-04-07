"""A simple program for compare two words an determin if these are equal or an anagram

-asks the user for two separate texts.
-checks whether, the entered texts are anagrams and prints the result
-assume that two empty strings are not anagrams.
-treat upper- and lower-case letters as equal
-spaces are not taken into account during the check, treat them as non-existent

"""

# Main function
def main():
    # Ask for the two words
    word_01: str = input("Enter the first word: ")
    word_02: str = input("Enter the second word: ")

    # If bouth are empty strings, print not an anagram
    if word_01 == "" and word_02 == "":
        print("Not an anagram")
    
    # Otherwise, continue
    else:
        # Call the check_anagram function
        p_word_01, p_word_02 = check_anagram(word_01, word_02)
        
        # Compare bouth strings
        if p_word_01 == p_word_02:
            print("Anagram")
        else:
            print("Not an anagram")


# Check anagram function
def check_anagram(word_01: str, word_02: str) -> str:
    """A function for procesing two strings and return it in lower case, without spaces and sorted"""
    
    # Get rid of initial and final spaces and convert to lower case letters
    s_word_01: str = word_01.strip().lower()
    s_word_02: str = word_02.strip().lower()
    
    # Convert both words to a list and sorted it
    l_word_01: list[str] = sorted(list(s_word_01))
    l_word_02: list[str] = sorted(list(s_word_02))

    # Convert sorted lists into a string
    p_word_01: str = "".join(l_word_01)
    p_word_02: str = "".join(l_word_02)

    return p_word_01, p_word_02


if __name__ == "__main__":
    main()
