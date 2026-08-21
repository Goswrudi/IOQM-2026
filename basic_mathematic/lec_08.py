# Alright Now Moving to the level 3 the divisiblity thinking 
# Now our battle gonnna be legnedry 

'''
🟠 Level 3 — Divisibility thinking

6. Without calculating the huge number, determine whether

3∣(10
50
+8)

Hint:

10≡1(mod3)

7. Find the remainder when

10
20
+10
5
+13

is divided by 9.

Hint:

10≡1(mod9)
'''


a = (10**50 + 8) % 3
b = int(input(f'enter divisor (try: 3) : '))

r = a % b
q = a // b

print(f"The Quouteint is ({q})")
print(f"The Remainder is ({r})")

if r == 0:
    print("Result: True (It is perfectly divisible!)")
else:
    print("Result: False (There is a remainder!)")