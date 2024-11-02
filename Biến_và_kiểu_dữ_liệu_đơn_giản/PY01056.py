from math import *


def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)):
        if n % i == 0:
            return False
    return True


def check(s):
    sum = 0
    for i in range(0, len(s)):
        tmp = int(s[i])
        if i & 1 == 1 and tmp & 1 == 0:
            return False
        elif i & 1 == 0 and tmp & 1 == 1:
            return False
        sum += tmp
    return prime(sum)


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        if check(s):
            print("YES")
        else:
            print("NO")
