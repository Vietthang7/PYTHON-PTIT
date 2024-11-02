from math import *


def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def check(s):
    k = int(s[:3])
    t = int(s[-3::])
    if prime(k) and prime(t):
        return True
    return False


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        if check(s):
            print("YES")
        else:
            print("NO")
