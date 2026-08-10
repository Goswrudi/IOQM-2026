'''

AP: Airthemtical Progression 

'''
# Probelm # 1:


'''
🟢 Level 1 — AP Detector
Problem 1 — Is it an AP?

Write:

is_ap(sequence)

that returns True if the sequence is an AP and False otherwise.

Examples:

[2, 5, 8, 11, 14] → True
[3, 7, 11, 15] → True
[1, 2, 4, 8] → False

Bonus: Return the common difference if it is an AP.

'''

def is_ap(sequence):
    x = sequence
    # y = [3, 7, 11, 15] 
    # z = [1, 2, 4, 8]

    # two consecutive terms is always a constant value. For example, in the sequence 2, 5, 8, 11, the difference is always constant : Therefore if  d = same , ap is true , else: false   
    d = x[1] - x[0] # output : 3
    d2 = x[2] - x[1] # output : 3
    d3 = x[3] - x[2] # output : 3
    
    print(f'{(d)} , {(d2)} , {(d3)} : Therefore D is same (We can say that is this a AP) ')

    if(d == d2) and (d2 == d3):
        return True

    return False

print(is_ap([2, 5, 8, 11, 14]))    


'''
🟢 Problem 2 — Generate the AP

Given:

a=7,d=4,n=10

Write a program that generates the first n terms.

Expected:

7 11 15 19 23 27 31 35 39 43

Then modify your program so the user can enter a, d, and n.
'''



def prob_2():
    a = 7
    d = 4
    n = 10

# Tried in Attempt 1

# solution = a + (n-1) * d

# print(solution)

# for solution in range(n):
#     solutionx = solution + d
#     print(solutionx)

    value = a

    for i in range(n):
        print(value)
        value += d

    # Solving the 2nd part of the problem ;


# Wrap input() inside int() to convert text to integers


    a1 = int(input('Enter (a) number: '))
    d1 = int(input('Enter (d) number: '))
    nn = int(input('Enter (n) number: '))

# Now you can perform math operations without errors
    print(f"First term: {a1}, Difference: {d1}, Total terms: {nn}")

    value = a1

    for x in range(nn):
        
            print(value)
            value += d1


prob_2()


'''
🟢 Problem 3 — Find the nth Term

Write:

nth_term(a, d, n)

using:

a
n
	​

=a+(n−1)d

Example:

nth_term(5, 3, 20)

Output:

62
🔥 Constraint

Don't generate all 20 terms. Calculate the answer directly.


'''


def n_term(a, d, n):
    return a + (n-1) * d


n_term(1 , 4 ,  4)

    

