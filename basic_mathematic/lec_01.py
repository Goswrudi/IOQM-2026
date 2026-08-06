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
