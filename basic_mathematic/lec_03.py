'''
🟢 Problem 1 — Find All Solutions

Find all positive integer solutions of:

x+y=20

Write a Python program that prints every possible pair (x, y).

Expected structure:

(1, 19)
(2, 18)
...
(19, 1)
Constraint

Don't manually write the answers. Make Python search for them.

Hint: What values can x take?
'''

# Problem 1

def prob_1():

    for x in range(21):
        y = 20 - x
        if y > 0:

            print(f'The Solutions are ({x},{y})')

prob_1()
# Problem 2
'''
🟢 Problem 2 — A Slight Upgrade

Find all positive integer solutions of:

2x+3y=20

Your program should print:

x = ?
y = ?

for every valid solution.

Important:

Don't just brute-force huge numbers.

Think about the fact that:

2x+3y=20

means once you choose x, what happens to y?

'''
print('')
# Problem 2

def prob_2():
    for i in range(1, 20):

        j = (20 - 2*i) / 3
        if j > 0 and j.is_integer():

            print(f'solutions are (int{j},{i})')

prob_2()

'''
🟡 Problem 3 — The Classic

Find all non-negative integer solutions of:

3x+5y=30

Your Python program should output every solution.

Then calculate:

Number of solutions = ?
Bonus 🔥

Modify your program so that it works for any equation:

ax+by=c
'''

def prob_3():
    count = 0
    for i in range(0 , 30):
        j = (30 - 5 * i) / 3
        if j >= 0 and j.is_integer():
            print(f'Solutions are : x=({j}) , y = {i})')
            count += 1

    print("Number of solutions:", count)


prob_3()