maths_constants = [['Euler Number', 2.7182],
 ['Golden Ratio', 1.618], 
 ['Imaginary Unit', '1j'], 
 ['Euler\'s identity', 'e^(iπ) + 1 = 0'], 
 ['Phi', 1.618033988749895], 
 ['Gamma Function', -0.08333333333333333], 
 ['Pi'],
 ['Riemann Zeta Function', 1.202056903159594], 
 ['Euler Formula', 'e^(ix) = cos(x) + i*sin(x)']
 ]
odd_list = [99,101,103,105,107,109]
even_string = '24689'

students = [['Gabriel', '53', '18', 'D', 'English'],
 ['Nora', '79', '18', 'F', 'Math'],
 ['Luna', '2', '18', 'A', 'English'],
 ['Anthony', '76', '18', 'A', 'Math'],
 ['Logan', '56', '17', 'D', 'History'],
 ['Luna', '20', '18', 'A', 'Math']]


#Find the index of an element inside a list
def find_index (input_list, element):
    index_pi = input_list.index([element])

    return index_pi

#Insert a value ona given list
def func_insert (input_list, index, value):
    input_list[index].insert(index, value)# .insert (index postion, value to add)

    return input_list


# Add separeted characters of a strig to a list
def add_sep_str (input_list, string_01):
    input_list.extend(string_01)
    
    return input_list

#Checking the elements of a list according to its index
def checking_e (input_list, index_01, index_02, r_01, r_02):
        element_01 = input_list[index_01][r_01]
        element_02 = input_list[index_02][r_02]
    
        print(f"element_01: {element_01} & element_02: {element_02}")


#Get a lis ofan element from a list of lists
def get_element (input_list, element):
        elements_list = [e[element] for e in input_list]

        return elements_list


#Find unique elemnts in a list that beging with a specific str
def spc_str (input_list, str):
        elements_with_str = []

        for e in input_list:
             if e[0][0] == str:
                elements_with_str.append(e)

        unique_elements_with_str = []

        for e in elements_with_str:
            if e not in unique_elements_with_str:
              unique_elements_with_str.append(e)

        print(len(unique_elements_with_str))

#Count particular elements in a list
def count_e (input_list, a, b):
    
    element_to_count = [a, b]
    count = 0   

    for e in input_list:
        if e[0] == element_to_count[0] and e[2] == element_to_count[1]:
            count += 1

    print(count)
               


def main():
    
    print (find_index (maths_constants, 'Pi'))
    print (func_insert (maths_constants, 6, 3.1416))
    print (add_sep_str (odd_list, even_string))
    print (checking_e (students, 3, 4, 0, 4))
    print (get_element (students, 2))
    print (spc_str (students, "A"))
    print (count_e (students, "Luna", "18"))


if __name__ == "__main__":

    main ()