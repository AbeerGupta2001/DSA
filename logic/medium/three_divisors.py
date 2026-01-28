



def threeDivisor(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = isPrime[1] = False

    for i in range(2,int(n ** 0.5)+1):
        if isPrime[i]:
            for j in range(i * 2, n+1 , i):
                isPrime[j] = False
    
    return isPrime

def countDivisor(n=16):
    total = 0
    isPrime = threeDivisor(n)

    for i in range(2,int(n ** 0.5)+1):
        if isPrime[i]:
            total += 1
    
    return total


if __name__ == "__main__":
    n = 100
    print(countDivisor(n))