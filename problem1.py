def solve():
    solution = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            solution +=i
    return solution

if __name__ == '__main__':
    print "Solution is:%s" % solve()
