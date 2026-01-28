


def valid_triangle(a,b,c):
    if (a+b) > c and (b+c) > a and (a+c) > b:
        return True
    else:
        return False
    
print(valid_triangle(7,10,5))