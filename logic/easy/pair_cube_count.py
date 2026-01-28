

import math


def pair_cube_count(n):
    count = 0
    for i in range(1,int(math.pow(n,1/3))+1):
        cb = i * i * i
        diff = n - cb
        cb_diff = round(diff ** (1/3))

        if cb_diff * cb_diff * cb_diff == diff:
            count+=1
    return count

print(pair_cube_count(126))