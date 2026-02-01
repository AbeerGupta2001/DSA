



def modular_exp(x=3,n=2,M=4):
    res = 1
    while n >= 1:

        if n % 2 == 1:
            res = (res * x) % M
            n -= 1
        else:
            x = (x * x) % M
            n //= 2
    
    return res


if __name__ == "__main__":
    x,n,M = 3,2,4
    print(modular_exp())