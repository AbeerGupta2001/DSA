

def power_set(s="ab"):
    n = len(s)
    res = []
    for i in range(int(2 ** n)):
        temp = ""
        for j in range(n+1):
            if i & (1 << j):
                temp += s[j]
        
        res.append(temp)
    
    return res

print(power_set())