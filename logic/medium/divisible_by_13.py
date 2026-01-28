



def divisible_by_13(n=2911285):
    temp = str(n)
    rem = 0
    for s in temp:
        d = int(s)
        rem = (rem * 10 + d) % 13
    
    return rem == 0


if divisible_by_13():
    print("The number is divisible by 13")
else:
    print("The number is not divisible by 13")
