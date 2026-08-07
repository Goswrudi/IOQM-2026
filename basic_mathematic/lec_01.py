# I just completed the Unacademy lectture 01 Sets of basic Mathematics by PJ sir !!
# Therefore asked Chatgpt to give me some problems which i can solve via python !!

'''
Problem

Given a list of numbers, print only the unique numbers while preserving their first appearance.

Input
[5, 3, 5, 2, 3, 8, 8, 1]

'''

sat = [5, 3, 5, 2, 3, 8, 8, 1]

seen = set()
duplicates = set()

for items in sat:
    if items in seen:
        duplicates.add(items)
    else:
        seen.add(items)

print(list(duplicates))



'''
Problem 2 — Common Students

Two classes have these roll numbers:

A = [1,2,3,4,5,6]
B = [4,5,6,7,8]

Find:

Common students
Students only in A
Students only in B

You can use Python's set for this one.

'''

A = [1,2,3,4,5,6]
B = [4,5,6,7,8]

set_A = set(A)
set_B = set(B)

common_numbers = set_A.intersection(set_B)
onlyA = set_A.intersection(set_B)
onlyB = set_B.intersection(set_A)

print(f'common numbers are {common_numbers}')
print(f'studnts only in A are {set_A}')
print(f'students only in B are {set_B}')


'''
🟡 Problem 3 — Guess the Set

Write a function:

def classify(A, B):
    ...

It should print whether:

A is a subset of B
B is a subset of A
They are equal
They are disjoint
None of the above

Example:

A={1,2}

B={1,2,3}

Output

A is subset of B
'''

import random

list_C = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
list_D = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) 

C = random.randint(1 , 10)
D = random.randint(1, 10)

x = random.choice(list_C)
y = random.choice(list_D)

#  Convert the numbers to strings, put them in a list, and join with a comma
combined_C = ",".join([str(C), str(x)])
combined_D = ",".join([str(D), str(y)])

print(combined_C)  
print(combined_D)  

# Creating the function for classification 

def classify():
    set_C = set(combined_C)
    set_D = set(combined_D)

    # Internal Problem : 
    # After trying sevral methods of flow control the program is unable to tell the computer what is left side what is right side!! which is important if i want to guess the subest!!

    # May this method will work 

    x , y = set_C
    w , z = set_D

    print("The computer knows x is:", x) 
    print("The computer knows y is:", y)
    print("The computer knows w is:", w) 
    print("The computer knows z is:", z)
     
classify()