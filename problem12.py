def triangle_num_gen(n):
    current_sum = 0
    for i in range(1,n+1):
        current_sum +=i
        yield current_sum

def get_divisors(n):
    divisors = []
    for i in range(1,n):
        if n%i ==0:
            divisors.append(i)

    return divisors
if __name__ == "__main__":
    for i in triangle_num_gen(200000):
        if i%2 != 0 or i%3 != 0 or i%5 != 0 or i%7 != 0 or i% 11 !=0:
            continue
        divisors = get_divisors(i)
        if len(divisors) >= 500:
            print "number was %d" % i
            print divisors
            break
