from math import sqrt
from math import ceil
'''
This simply generates the first n primes
'''

def generate_primes(n):
    '''This will generate the first n primes'''
    if n == 0:
        return []

    primes = [2]
    while True:
       if len(primes) == n:
          return primes
       primes.append(generate_next_prime(primes[-1],primes))


def generate_primes_up_to(n):
    '''This will generate all the primes up to the number n'''
    if n == 0:
        return []

    primes = [2]
    while True:
       if primes[-1] == n:
           return primes
       if primes[-1] > n:
           return primes[0:-1]

       primes.append(generate_next_prime(primes[-1],primes))


def generate_next_prime(n, existing_primes):
    '''This will generate the next prime higher than n using existing primes'''
    if n % 2 == 0:
        candidate = n+1
    else:
        candidate = n+2

    while True:
        could_be = True
        limit = ceil(sqrt(candidate))+1
        for prime in existing_primes:
            if prime > limit:
                return candidate    
            if candidate % prime == 0:
                could_be = False
                break
        if could_be:
            return candidate

        candidate += 2

    return candidate 

if __name__ == "__main__":
    print generate_primes(100)
