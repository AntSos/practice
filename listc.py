#List Comprehension
#List comprehension offers a shorter syntax when you want to create 
#a new list based on the values of an existing list.


    #newlist = [expression for item in iterable if condition == True]



def convert_to_snake_case_01(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    snake_cased_string = ''.join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip('_')

    return clean_snake_cased_string



def convert_to_snake_case_02(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print("Regular list: ", convert_to_snake_case_01('aLongAndComplexString'))

    print("Comprehension list: ", convert_to_snake_case_02('IAmAPascalCasedString'))

if __name__ == '__main__':
    main()