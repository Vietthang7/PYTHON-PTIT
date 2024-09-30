from math import *


def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def sumDigit(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return nt(sum)


if __name__ == "__main__":
    t = int(input())
    while t != 0:
        a, b = map(int, input().split())
        if sumDigit(gcd(a, b)):
            print("YES")
        else:
            print("NO")
        t -= 1
