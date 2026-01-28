

# Exact the repeating number


def repeating_number(a=8,b=3):
    res = ""
    rem = a % b
    
    if rem == 0:
        return "No repeating sequence"
    
    mp = {}

    while rem > 0:

        if rem in mp:
            res = res[mp[rem]:]
            break

        mp[rem] = len(res) 
        rem = rem * 10
        res += str(rem // b)
        rem = rem % b
    
    return res

if __name__ == "__main__":
    result = repeating_number(50,22)
    if result:
        print(result)
    else:
        print("No repeating sequence found")
