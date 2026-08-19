# Alright Moving something more 10/10 

# Now we are discovering divisiblity teorms and it's algorithm

'''
🟢 Level 1 — Warm-up

1. Use the Division Algorithm to write:

157=13q+r

Find q and r.
'''

def algo():

    a = int(input(f"Enter dividend: "))
    b = int(input(f"Enter divisor: "))

    q = a // b
    r = a % b

    print(f"The quoteint is: {q}")
    print(f"The remainder is: {r}")

#algo()



'''
2. Find:

83mod7

146mod11

250mod13

'''


def mod():
    x = int(input(f"enter the dividend: "))
    y = int(input(f"enter the divisor: "))

    modulo = x % y 

    print(modulo)

#mod()

# There is another way you can find mod manually 

def manualmod():
    x = int(input(f"enter the dividend: "))
    y = int(input(f"enter the divisor: "))

    d = x // y

    m = d * y

    s = x - m


    print(f"the quoteint is ({d}) , the closest multiple is ({m}) , the mod is ({s}) || ")

manualmod()