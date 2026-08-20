# This is the level 2 of divisblity algorithm and theorm problem solving we are getting some intermediate questions which ask for the logic and IQ instead of "parrot syntax"


# Here we go:

'''
🟡 Level 2 — Understand the theorem

4. Given:

7∣21,7∣35

show that:

7∣(4⋅21−3⋅35)

But don't just calculate the final number. Use the form:

21=7a,35=7b

and factor out 7.

5. Suppose

a∣b

Prove that:

a∣kb

for every integer k.

Tiny proof, but VERY important.
'''


def show():
    quoteint = []
    remainder = []

    for i in range(2):
        print(f"---- Input{i+1}")
        x = int(input('Enter the Dividend '))
        y = int(input('Enter the Divisor '))

        q = x // y
        r = x % y 

        quoteint.append(q)
        remainder.append(r)

    print(f'The quoteint of input 1 is: {quoteint[0]} and the Remainder is: {remainder[0]}')
    print(f'The quoteint of input 2 is: {quoteint[1]} and the Remainder is: {remainder[1]}')
 
show()

