"""
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

class CollatzProblemCalculator:
    _num_map = {1:1}
    
    def get_max_value(self):
        return max(self._num_map, key=self._num_map.get)
    
    def get_next_num(self, n):
        if n%2:
            return 3*n+1
        else:
            return n/2
    
    def get_total_for(self,n):
        next = self.get_next_num(n)
        if self._num_map.has_key(next):
            self._num_map[n] = self._num_map[next] + 1
        else:
            self._num_map[n] = self.get_total_for(next) + 1
        
        return self._num_map[n]

if __name__ == "__main__":
    calc = CollatzProblemCalculator()
    for i in range(2,1000000):
        calc.get_total_for(i)
        
    print calc.get_max_value()
    
