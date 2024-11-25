from math import *


def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    d = dict()
    for x in a:
        if prime(x):
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
    for val, fre in d.items():
        print(val, fre)
