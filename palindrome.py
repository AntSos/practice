
def palindrome (words):
    string_01 = words.replace (" ", "")
    string_02 = string_01.lower ()
    
    
    if string_02 [::-1] == string_02:
        print (f"Palindrome: {words}")

    else:
        print (f"Not palindrome: {words}")

def main ():
    input_words = input ("Write some words or numbers: ")
    print (palindrome (input_words))

if __name__ == "__main__":
    main ()