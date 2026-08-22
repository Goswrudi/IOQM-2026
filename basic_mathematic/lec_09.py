# Alrghit So now we moving like the ddragon baby of number thory knowns as Eucldeian Algorithm 
# Which is all about finding gcd(greatest common divisor) !!
# we tried to solve this as a automation and manuall way !!!

# Here we go automation way first !


def gcd():
    a = int(input(f"enter the dividend: "))
    b = int(input(f"enter the divisor: "))
    while b != 0:
        a , b = b , a % b 

    return a

print(f"The GCD IS : ({gcd()})")
