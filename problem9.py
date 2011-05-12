'''
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

from itertools import ifilter
import math

def get_all_trips_to(n):
    for i in range(1,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                yield (i,j,k)
     
if __name__ == '__main__':
    total = 1000
    sums_thousand = ifilter(lambda trip: sum(trip) == total, get_all_trips_to(total))
    
    for t in sums_thousand:
        squared = map(lambda tt: math.pow(tt,2),t)
        if squared[0] + squared[1] == squared[2]:
            print t[0] * t[1] * t[2]
            break
        
    
