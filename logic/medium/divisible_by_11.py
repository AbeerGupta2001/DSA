
# Find the sum of odd_place integers and even_place integers the odd_place - even_place. If the difference is divisible by 11 then is True else False



def divisible_by_11(n=1234567589333892):
    temp = str(n)
    even_sum = 0
    odd_sum = 0
    for i in range(len(temp)):
        d = int(temp[i])
        if i % 2 == 0:
            even_sum += d
        else:
            odd_sum += d
    
    return (odd_sum - even_sum) % 11 == 0

if __name__ == "__main__":
    if divisible_by_11():
        print("The number is divisible by 11")
    else:
        print("The number is not divisible by 11")