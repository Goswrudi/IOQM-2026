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