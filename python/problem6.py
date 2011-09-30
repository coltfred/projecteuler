import math

if __name__ == '__main__':
    nums = range(1,101)
    sum_of_squares = sum([math.pow(v,2) for v in nums])
    square_of_sums = math.pow(sum(nums),2)
    print square_of_sums - sum_of_squares
