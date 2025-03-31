"""PI course Lab: A led display"""


# List with the characters to draw number0-9
num_digits =[['###','# #','# #','# #','###'],#0
            ['  #','  #','  #','  #','  #'],#1
            ['###','  #','###','#  ','###'],#2
            ['###','  #','###','  #','###'],#3
            ['# #','# #','###','  #','  #'],#4
            ['###','#  ','###','  #','###'],#5
            ['###','#  ','###','# #','###'],#6
            ['###','  #','  #','  #','  #'],#7
            ['###','# #','###','# #','###'],#8
            ['###','# #','###','  #','###']#9
            ]

#User input
user_input = input('Enter a non-negative integer number: ')
    
#Print a row
for row in range(5):
    
    #Print each number given by user
    for num in user_input:
        print(num_digits[int(num)][row], end = ' ')
    
    print()