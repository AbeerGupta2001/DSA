


def all_factor(n = 10):

    res = []

    for i in range(1,int(n ** 0.5)+1):
        if n % i == 0:
            res.append(i)
            res.append(n // i)
    res.sort()

    return res


if __name__ == "__main__":
    res = all_factor(100)
    print(res)
