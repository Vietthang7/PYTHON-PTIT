from math import *


def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def check(s):
    for i in range(0, len(s)):
        check1 = prime(i)
        check2 = prime(int(s[i]))
        if check1 != check2:
            return False
    return True


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        if check(s):
            print("YES")
        else:
            print("NO")
