



def binary_search_method(n):
    low = 1
    high = n
    res = 1

    while low <= high:
        mid = (low + high) // 2

        if mid * mid <= n:
            res = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return res 


if __name__ == "__main__":
    n = 11
    print(binary_search_method(n))