# Alrghit So now we moving like the ddragon baby of number thory knowns as Eucldeian Algorithm 
# Which is all about finding gcd(greatest common divisor) !!
# we tried to solve this as a automation and manuall way !!!

# Here we go automation way first !


def gcd(a , b):
    while b != 0:
        a , b = b , a % b 

    return a

print(gcd(48 , 18))