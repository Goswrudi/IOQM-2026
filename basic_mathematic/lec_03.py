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

for x in range(21):
    y = 20 - x
    if y > 0:
        print(f'The Solutions are ({x},{y})')

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

