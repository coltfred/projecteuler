import math


def triangle_num_gen(n):
    current_sum = 0
    for i in range(1,n+1):
        current_sum +=i
        yield current_sum

def get_divisors(n):
    divisors = []
    for i in range(1,int(math.sqrt(n))+1):
        if n%i ==0:
            divisors.append(i)
            divisors.append(n/i)

    return divisors
if __name__ == "__main__":
    for i in triangle_num_gen(200000):
        divisors = get_divisors(i)
        if len(divisors) >= 500:
            print "number was %d" % i
            print divisors
            break
