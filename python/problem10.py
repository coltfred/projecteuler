'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from prime_gen import generate_primes_up_to

if __name__ == "__main__":
   print sum(generate_primes_up_to(2000000))
