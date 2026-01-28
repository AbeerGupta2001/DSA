# if the input is a large number then take only last two digit and see if it is divisible by 4. If True then the number is divisible by 4 or not.

def divisible_by_4(n=1124):
    temp = str(n)
    if len(temp) == 0:
        return False
    
    if len(temp) == 1:
        return int(temp) % 4 == 0    
    last_two = temp[-2:]

    if int(last_two) % 4 == 0:
        return True
    return False


if __name__ == "__main__":
    n = 12
    if divisible_by_4(n):
        print(f"The number {n} is divisible by 4")
    else:
        print(f"The number {n} is not divisible by 4")