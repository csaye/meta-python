i = 2
while i < 100: # prints primes up to 100
    prime = 1
    upper = i ** 0.5 + 1
    j = 2
    while j < upper:
        if i % j == 0:
            prime = 0
        j += 1
    if prime == 1:
        print(i)
    i += 1
