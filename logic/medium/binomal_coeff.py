


def binomialCoeff(n,r):
    if r > n:
        return 0
    
    if r == 0 or r == n:
        return 1
    
    return binomialCoeff(n-1,r-1) + binomialCoeff(n-1,r)

def memoization_topDownDp(n,k,memo):

    if k > n:
        return 0
    
    if k == 0 or k == n:
        return 1
    

    if memo[n][k] != -1:
        return memo[n][k]

    memo[n][k] = memoization_topDownDp(n-1,k-1,memo) + memoization_topDownDp(n-1,k,memo)

    return memo[n][k]

n = 5
k = 2
print(binomialCoeff(n,k))
memo = [[-1 for _ in range(k+1)] for _ in range(n+1)]
print(memoization_topDownDp(n,k,memo))