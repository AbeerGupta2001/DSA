



def decimal_to_binary(n):
    res = ''
    while n != 0:
        res = str(n % 2) + res
        n = n // 2
    
    return res

print(decimal_to_binary(33))