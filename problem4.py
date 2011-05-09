def is_pal(s):
    length = len(s)
    half = length/2
    return s[0:-half] == s[half:length][::-1]

if __name__ == '__main__':
    i = 999
    j = 999
    ans = 0
    while i > 0:
        while j > 0:
            temp = i*j
            if is_pal(str(temp)):
                if temp > ans:
                    ans = temp
                else:
                    break;
            j += -1
        i += -1
        j = 999
    print ans
