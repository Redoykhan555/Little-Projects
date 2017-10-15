p=0
import time 
def sieve(n):
    sieve = [True] * int(n/2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::i] = [False] * int((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in range(1,int(n/2)) if sieve[i]]


#generator version
def prime_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False
    for n in range(2, limit, 2):     # Mark factors non-prime
        a[n] = False
    yield 2
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, 2*i):     # Mark factors non-prime
                a[n] = False


q=time.clock()
p=sieve(100000000)
z=time.clock()
print(z-q)
