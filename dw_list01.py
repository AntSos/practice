
input_list = [2, 2, 3, 4, 5, 6, 6, 6]

input_list_1 = [2, 2, 3, 4, 5, 6, 8, 9, 10]
input_list_2 = [2, 3, 4, 5, 6, 6, 6, 10, 12]
input_list_str = ['e', 'd', 'f', 'a', 'c', 'b']
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

#Find Unique elemnts in a list
def unique_list_elements_01 (input_list):
    unique_items = []
    for i in input_list:
        if i not in unique_items:
            unique_items.append (i)

    return unique_items
#Find Unique elemnts in a list Simple using set and transform it as a list
def unique_list_elements_02 (input_list):
    unique_items = list (set (input_list)) 
    return unique_items

#Find Common Elements in Two Lists
def get_common_01(input_list_1, input_list_2):
    common_items = []
    for item in input_list_1:
        if item in input_list_2:
            common_items.append(item)
    
    return common_items

#Find Common Elements in Two Lists with list comprehension
def get_common_02(input_list_1, input_list_2):
    common_items = [i for i in input_list_1 if i in input_list_2]
    
    return common_items

#Calculate Average of Numbers
def get_average_01(input_list):
    count = 0
    suma = 0
    for e in input_list:
        suma += e
        count += 1
    
    return float (suma/count)

#Calculate Average of Numbers
def get_average_02(input_list):
    total_items = len(input_list)
    sum_total = sum(input_list)
    average = sum_total/total_items
    return average

#Sort Strings Alphabetically
def sort_alphabets(input_list_str):
    sort_a_list = sorted (input_list_str)
    return sort_a_list

#Square Numbers in a List list comprenhension
def square_list(input_list):
    list_square = [i*i for i in input_list]
    return list_square

#Count the lenght of every element in a list and return it
def count_len(input_list):
    count = [len (i) for i in input_list]# Return lenght of i fr every item inside the list
    return count

#Search and reaplace a string in a list
def str_search_and_replace (input_list):
    str_search = "mango"
    str_replace = "pears"
    mod_list = []
    for i in range(len(input_list)):
        if input_list[i] == str_search:
            input_list[i] = str_replace
    
    return input_list

#Search and count an element in a list
def serch_and_count (input_list):
    item = "apple"
    count = 0
    for e in input_list:
        if e == item:
            count += 1
    
    return count


#Find the shortes and longest str inside a list 
def shrts_lngst_str_01 (input_list):
    length_list = [len (i) for i in input_list]

    shortest_str = min (length_list)
    longest_str = max (length_list)

    print (f'Shortest str: {shortest_str}, Longest str: {longest_str}')

#Find the shortes and longest str inside a list and print the str with its length number
def shrts_lngst_str_02 (input_list):
    shortest_str = input_list[0]
    longest_str = input_list[0]

    for i in input_list:
        if len(i) < len(shortest_str):
            shortest_str = i

        if len(i) > len(longest_str):
            longest_str = i

    print(f"Longest str : {longest_str} is {len(longest_str)}\nShortest str : {shortest_str} is : {len(shortest_str)}")


def main ():
    print (unique_list_elements_01(input_list))
    print (unique_list_elements_02(input_list))
    print (get_common_01(input_list_1, input_list_2))
    print (get_common_02(input_list_1, input_list_2))
    print(get_average_01(input_list))
    print(get_average_02(input_list))
    print (sort_alphabets(input_list_str))
    print (square_list(input_list))
    print (count_len(fruits))
    print (f'Original: {fruits}')
    print ("Replaced: ", str_search_and_replace (fruits))
    print (serch_and_count (fruits))
    print (shrts_lngst_str_01 (fruits))
    print (shrts_lngst_str_02 (fruits))

if __name__ == "__main__":
    main ()
