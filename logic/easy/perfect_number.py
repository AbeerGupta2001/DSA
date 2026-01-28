


def perfect_number(n):
    sum = 1
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            if i * i != n:
                sum += i + n // i
            else:
                sum += i
    
    return sum == n and n != 1


if __name__ == "__main__":
    n = int(input("Enter a number:"))
    if perfect_number(n):
        print("It is a perfect number")
    else:
        print("It is not a perfect number")