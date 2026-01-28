#Find a number close to n and divisible by m 

import math

def closest_num(n,m):
    q = int(n / m)
    # 1st possible closest number
    n1 = m * q
    # 2nd possible closest number
    if((n * m) > 0) :
        n2 = (m * (q + 1)) 
    else :
        n2 = (m * (q - 1))
    
    # if true, then n1 is the required closest number
    if (abs(n - n1) < abs(n - n2)) :
        return n1
    
    # else n2 is the required closest number 
    return n2


print(closest_num(-15,6))