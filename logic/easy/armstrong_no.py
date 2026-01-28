

def armstrong(temp=153):
    sum = 0
    n = temp
    pow = len(str(temp))
    while n != 0:
        q = n % 10
        sum += int(q ** pow)
        n = n // 10
    
    return sum == temp


if __name__ == "__main__":
    if armstrong(9474):
        print("The number is armstrong")
    else:
        print("The number is not armstrong")
        