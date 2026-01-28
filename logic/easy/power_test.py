

import math

def power_test(x,y):
    res1 = math.log(y)/math.log(x)
    return res1 == math.floor(res1)

print(power_test(10,10000))