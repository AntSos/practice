#Sets are defined using curly braces {} or the set() constructor
#you cannot index elements in a set in Python because sets are unordered 
#collections of unique elements. 

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = set ([1, 3, 4, 5, 6])

#To take the union use the union() method or the | operator

s1_union_s2 = s1 | s2
s1_union_s3 = s1.union(s2)

#The intersection of two sets operator & or method intersection ()
s1_intersection_s2 = s1 & s2
s1_intersection_s3 = s1.intersection (s2)

#Difference  use the - operator or the difference() method
s1_difference_s2 = s1-s2
s1_difference_s3 = s1.difference (s2)

# Subset usethe method issubset ()
s1_subset_s2 = s1.issubset (s2)

# For simetric use the the ^ operator or symmetric_difference() method or
s2_symmetric_difference_s1 = s1 ^ s2
s2_symmetric_difference_s1 = s1.symmetric_difference(s2)

#To add elemnts to a set use the method add ()
s2.add (24)
print (s2)
#To remove use temethod remove () or discard ()
s2.remove (24)
print (s2)

# Add severallemns in a set at once use operators |= or method update([])
s3 |= {21,35,36}
print (s3) 

#To sort a set use sorted (set, reversed = False)
print (sorted (s3, reverse = False))

#For clear a set use the method .clear ()
print (s3.clear ())
word = "Hello"
word_set = set (word)
print (word_set)
print (len (word_set))


