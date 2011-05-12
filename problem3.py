import math 
'''What is the largest prime factor of the number 600851475143 ?'''
def IsPrime( n ): 
    if n == 2: 
        return True 
    elif n % 2 == 0: 
        return False 

    divisor = 3 
    range = math.ceil(math.sqrt(n))
    while( divisor < range ): 
        if( n % divisor == 0): 
            return False 
        divisor += 1 
    return True 

    
if __name__ == "__main__":
    num = 600851475143
    next_check = math.ceil(math.sqrt(num)) + 1
    
    while True: 
        if num % next_check == 0 and IsPrime(next_check): 
            break
        next_check += -1
    print next_check 