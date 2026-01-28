


def kthDigit(a=3,b=3,k=1):

    temp = str(a ** b)

    if k > len(temp):
        return -1
    
    return temp[-k]


if __name__ == "__main__":
    
    print(kthDigit(a=5,b=2,k=2))