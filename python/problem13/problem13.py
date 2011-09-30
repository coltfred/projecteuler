'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
see input for numbers
'''
import sys

def read_input(data_file='./input.txt'):
    try:
        f = open(data_file,'r')
        if not f:
            return False
    except Exception, e:
        return False

    return map(lambda x: long(x[0:-1]),f.readlines())
    




if __name__ == "__main__":
    numbers = read_input()

    if not numbers:
        print "File couldn't be read"
        sys.exit(1)

    print str(sum(numbers))[0:10]
