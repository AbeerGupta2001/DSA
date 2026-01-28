

# Approach 1
def prime_factor(n):
    res = []

    if n  % 2 == 0:
        res.append(2)
        while n % 2 == 0:
            n //= 2
    

    i = 3
    while i * i <= n:
        if n % i == 0:
            res.append(i)
            while n % i == 0:
                n //= i
        
        i += 2
    
    if n > 2:
        res.append(n)
    
    return res

# Approach 2
def smallest_prime_factor(n):
    spf = [i for i in range(n+1)]

    for i in range(2,int(n ** 0.5)+1):
        if spf[i] == i:
            for j in range(i*i,n+1,i):
                if spf[j] == j:
                    spf[j] = i
    
    return spf

def prime_factors(n,spf):
    prime_max = 1

    while n > 1:
        prime_max = max(prime_max,spf[n])
        n //= spf[n]
    
    return prime_max

# def square(x):
#     return x * x

if __name__ == "__main__":
    n = 28
    temp = [1,2,3,4,5,6]
    # Approach 1
    # res = prime_factor(n)
    # print(" ".join(map(str,res)))

    # Approach 2
    spf = smallest_prime_factor(n)
    res = prime_factors(n,spf)
    print(res)
    # print(" ".join(map(str,res)))
    
    
    # obj = list(map(square,temp))
    # print(obj)