

def sum_of_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)

    return sum

print(sum_of_digits(687))