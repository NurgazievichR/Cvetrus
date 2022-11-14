from sympy import simplify

primes = [i for i in range(1,10001) if simplify(i).is_prime]
for x in primes:
    for y in primes:
        if y**2-x**2-23*y+x+132==0:
            print(f'x:{x} | y:{y}')

