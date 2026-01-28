

def palindrome(n=12321):
    temp = str(n)
    l = len(temp)
    for i in range(l // 2):
        if temp[i] != temp[l - i -1]:
            return False
    
    return True

if __name__ == "__main__":
    if palindrome(1234):
        print("The number is palindrome")
    else:
        print("The number is not palindrome")