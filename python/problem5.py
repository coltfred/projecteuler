def is_div_by_all_up_to(x, max_div):
    for i in range(1, max_div+1):
        if x % i != 0:
            return False
    return True

if __name__ == '__main__':
    max_div = 20
    i = max_div
    while True:
        if is_div_by_all_up_to(i, max_div):
            ans = i
            break
        i+=max_div
    print ans
