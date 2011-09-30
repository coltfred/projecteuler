def fib_up_to(x):
    lookup = [0,1]
    while lookup[-1] < x:
        lookup.append(lookup[-1] + lookup[-2])

    return lookup[0:-1]

if __name__ == '__main__':
    print sum([v for v in fib_up_to(4000000) if not v%2])
