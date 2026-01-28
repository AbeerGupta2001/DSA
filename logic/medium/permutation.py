

def factorial(n):
    rem = 1
    for i in range(2,n+1):
        rem = rem * i
    
    return rem


def permutation(n=5,r=2):
    n_factorial = factorial(n)
    n_r_factorial = factorial(n -r)

    return n_factorial // n_r_factorial

print(permutation(6,3))