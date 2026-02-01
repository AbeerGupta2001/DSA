

# Binomial Coefficient

def binomialCoeff(n,k):

    ans = 1

    if k > n - k:
        k = n - k

    
    for i in range(k):
        ans *= (n - i)
        ans //= (i+1)
    
    return ans


def findCatalan(n):

    c = binomialCoeff(2 * n,n)
    return c // (n+1)

n = 6
res = findCatalan(n)
print(res)