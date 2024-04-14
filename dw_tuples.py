# Tuples are immutable data structures in Python that allow you to store a collection of items.
#They are similar to lists, but the main difference is that tuples cannot be modified once 
#created. Tuples are defined using parentheses () or the tuple() function.

#Tuples can contain elements of different data types, such as numbers, strings, or even other 
#tuples. The elements in a tuple are ordered and can be accessed using indexing. 

# Function map()could be used to convert every elemnt in a tuple to integers and then get a value from them

my_t1 = ("1", "2", "3")

my_t1_int = max (map (int, my_t1))

print (my_t1_int)

# Concatenate 2 tuples
my_t2 = ("4", "5", "6")
my_t3 = my_t1 + my_t2
print (my_t3)

students = ((1, 2, 3), ('Carlos Green', 'Joseph Mendoza','Todd Johns'), ('1818 Guzman Court Suite 712', 'IN 32206','80276 Paul Trace\nSouth'), ('A','A','C'))
my_t4 = (1,2,3,4,5,6,7,8,9,10,11)

# Loop and print trougth the tuple
def loop_tuple (input_tuple):
    for e in range(len (input_tuple[0])): #Indicate and pass the len of the first tuple students[0]
        print(f"Student ID: {input_tuple[0][e]}")
        print(f"Name: {input_tuple[1][e]}")
        print(f"Address: {input_tuple[2][e]}")
        print(f"Grade: {input_tuple[3][e]}")
        print("-" * 30)  # Separator between students

# Count a element inthe tuple of tuples
def count_e (input_tuple):
    grade_count = 0

    for e in students [3]:# Welook for the grade, so we usethe 3 index
        if e == "A":
            grade_count += 1
    return grade_count

#Acces to students name with a requiered grade
def name_s (input_tuple, g):
    
    t_students = tuple ()

    for e, grade in enumerate (input_tuple [3]):# Use enumerate to give a number (e) to the grade in the tuple
        if grade == g:
            t_students += (input_tuple [1][e],)# Add a tuple to t_students with the students index [1][e]
        
    return tuple (sorted (t_students))# Return a sorted tuple 

# Split a tuple with comprehension
def split (input_tuple):
    first_half = tuple(e[:5] for e in input_tuple)
    second_half = tuple(e[5:] for e in input_tuple)

    print (first_half)
    print (second_half)


# Find the adress of a given student
def s_adress (input_tuple, name):

    for e, x in enumerate (input_tuple [1]):# Use enumerate to give a number to the element in the tuple e = to the number and x the elemnt in the tuple
        if x == name:# As we are looking for the index o a given name, wewill use 2 elemnts: e = the number given by enumerate and x is the name that we are looking
            print (input_tuple [2][e])# Then we will print the [2][e] second tuple wit adress, and e the number that match with the name we are looking


def main ():
    print (loop_tuple (students))
    print (count_e (students))
    print (name_s (students, g = "A"))
    #print (split (my_t4))
    print (s_adress (students, name = "Todd Johns"))


if __name__ == "__main__":
    main ()