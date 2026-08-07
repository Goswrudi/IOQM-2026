# Moving to Algebra Now :

'''
🟢 Problem 1 — Frequency Counter

Given:

nums = [2,1,2,3,1,4,2,5,3]

Print:

2 -> 3 times
1 -> 2 times
3 -> 2 times
4 -> 1 time
5 -> 1 time

Challenge: Don't use collections.Counter.

'''

nums = [2,1,2,3,1,4,2,5,3]
freq = {}

count = nums.count

for num in nums:
    if num in freq:
        freq[num] = +1
    else:
        freq[num] = 1

for key, value in freq.items():
    if value == 1:
        print(f"{key} -> {value} time")
    else:
        print(f"{key} -> {value} times")



'''
🟢 Problem 2 — Set Relationship Checker

Write a function:

relationship(A, B)

that returns one of:

"Equal"
"Subset"
"Superset"
"Disjoint"
"Intersecting"

Notice "Intersecting" is new—it means they share some elements but none of the other relationships apply.
'''