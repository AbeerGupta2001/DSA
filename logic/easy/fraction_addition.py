

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)

def lcm(a,b):
    return int(a * b / gcd(a,b))

def fraction_add(a = [1, 5] , b = [3, 15]):
    num_lcm = lcm(a[1],b[1])
    val1 = a[0] * int(num_lcm // a[1])
    val2 = b[0] * int(num_lcm // b[1])
    sum = val1 + val2
    
    val3 = gcd(sum,num_lcm)
    
    return [int(sum//val3),int(num_lcm//val3)]
    


print(fraction_add())