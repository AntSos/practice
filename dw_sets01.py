data_novice = set (['Obe', 'Alexande', 'Ellwood', 'Antwan', 'Ferne, "Elvia"'])
data_explorer = set (['Velva', 'Rachel', 'Everette', 'Madalynn', "Elvia", 'Benton'])
analytics_enthusiast = set (['Elba', 'Eldridge', 'Nash', "Elvia", 'Bailey', 'Gerold'])
python_prodigy = set (['Lindbergh', 'Bronson', 'Aydin', 'Marcelina', 'Dorla'])
insight_seeker = set (['Woody', 'Ona', 'Alver', 'Opha', "Elvia", 'Sarah'])
data_detective = set (['Sonia', 'Verlyn', 'Blaze', "Elvia", 'Lizeth', 'Dalton'])
trend_tracker = set (['Lawton', 'Dean', 'Darrien', 'Tate', "Elvia", 'Tea'])
problem_solver = set (['Cher', 'Lynn', 'Brain', "Elvia", 'Jaymes', 'Gracie'])
data_ninja = set (['Dulce', 'Beryl', 'Braxton', 'Aubrey', "Elvia", 'Tayler'])
algorithm_apprentice = set (['Alonza', 'Ulises', 'Rohan', 'Roberta', "Elvia",  'Kathryne'])
data_wizard = set (['Kyan', 'Hilary', 'Bettie', 'Brittnee', 'Della', "Elvia"])
analytics_guru = set (['Rexford', 'Frederica', 'Rhys', 'Cathy', 'Daulton', "Elvia"])
statistic_sage = set (['Jimmy', 'Kamora', 'Raul', 'Marci', 'Pat', "Elvia"])
machine_learning_maestro = set (['Erika', 'Lemma', 'Courtney', 'Niki', 'Bula', "Elvia"])
data_scientist = set (['Adriane', 'Octavio', 'Jakayla', 'Pamelia', 'Kenna', "Elvia"])

data_test = {'Abbey','Adelard','Adison','Adolph','Aidan','Akira','Alan','Albertha','Aletha','Alexa','Alexander','Alfredo'}


all_badges = [data_novice, 
              data_explorer, 
              analytics_enthusiast, 
              python_prodigy, 
              insight_seeker, 
              data_detective, 
              trend_tracker, 
              problem_solver, 
              data_ninja, 
              algorithm_apprentice, 
              data_wizard, 
              analytics_guru, 
              statistic_sage,
              machine_learning_maestro, 
              data_scientist
              ]

#Eliminate a elemnt in a large list of diferent sets
def eliminate_element (input_set, element):

    for i in input_set:
        i.discard (element)
        
        return input_set


#Find the shortest and longuest namesin a set
def short_long_name (input_set):
    shortest_name = [name for name in input_set if len(name) == len(min(input_set, key=len))]
    longest_names = [name for name in input_set if len(name) == len(max(input_set, key=len))]

    # Display the results
    print(f"Shortest Name: {', '.join (sorted (shortest_name, reverse = False))}")
    print(f"Longest Names: {', '.join(sorted (longest_names, reverse = False))}")


# main function
def main ():

    #print (eliminate_element (data_scientist, element = "Elvia"))
    print (short_long_name (data_test))

if __name__ == "__main__":
    main ()