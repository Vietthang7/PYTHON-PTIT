from math import *


def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        sumDigit = 0
        for i in range(0, len(s)):
            sumDigit += int(s[i])
        if prime(sumDigit):
            print("YES")
        else:
            print("NO")
