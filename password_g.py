import re #It allows usto use regular expresions
import secrets
import string


def generate_password(length, nums, special_chars, uppercase, lowercase):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    password = ''
    # Generate password
    while True:
        password = ''
        for _ in range(length): # A standalone underscore is used to represent a value that wont be used
            password += secrets.choice(all_characters)
        
            constraints = [#Use raw strings is a good practice since they can contain a lot of \
                (nums, r'\d'),#The character class \d is a shorthand for [0-9]
                (lowercase, r'[a-z]'), 
                (uppercase, r'[A-Z]'),
                (special_chars, fr'[{symbols}]')#We interpolate a f string with the simbols variable
            ] 

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password


if __name__ == "__main__":

    new_password = generate_password( length= 30, nums = 6, special_chars = 3, uppercase = 3, lowercase = 9)

    print("Generated password: ", new_password)
