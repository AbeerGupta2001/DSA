


def repeating_decimal(a=50,b=22):
    if a == 0:
        return "0"
    
    res = "-" if (a < 0) or (b < 0) else ""

    a = abs(a)
    b = abs(b)

    res += str (a//b)

    rem = a % b

    if rem == 0:
        return res
    
    res += "."
    mp = {}

    while rem > 0:
        if rem in mp:
            res = res[:mp[rem]] + "(" + res[mp[rem]:] + ")"
            break

        mp[rem] = len(res)

        rem = rem * 10
        res += str(rem // b)
        rem = rem % b
    
    return res

print(repeating_decimal())