

import math

def prime_test(n):
    if n == 2 or n ==3:
        return True
    elif n <=1 or n % 2 ==0 or n % 3 == 0:
        return False
    for i in range(5,int(math.sqrt(n))+1,6):
        if n % i == 0 or n % (i+2) == 0:
            return False
        
    return True


if prime_test(11):
    print("Prime Number")
else:
    print("Not Prime Number")