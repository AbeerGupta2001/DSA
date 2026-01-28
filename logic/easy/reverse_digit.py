




def reverse_digit(n):
    s = str(n)

    # reversing the string
    s = s[::-1]

    # converting string to integer
    n = int(s)

    # returning integer
    return n

print(reverse_digit(123))