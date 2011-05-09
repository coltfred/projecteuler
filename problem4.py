def is_pal(s):
    length = len(s)
    half = length/2
    #print " checking %s against %s" % (s[0:-half],s[half:length][::-1])
    return s[0:-half] == s[half:length][::-1]

if __name__ == '__main__':
    i = 1000
    j = 1000
    ans = None
    while not ans and i > 0:
        i += -1
        while not ans and j > 0:
            j += -1
            temp = str(i*j)
            if is_pal(temp):
                ans = temp
                print "i was %d and j was %d:%s" % (i,j,ans)

        j = 1000

