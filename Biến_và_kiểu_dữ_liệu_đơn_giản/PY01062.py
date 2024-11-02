from math import *


def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def check(s):
    numberNgto = 0
    number = 0
    for i in range(0, len(s)):
        if prime(int(s[i])):
            numberNgto += 1
        else:
            number += 1
    return numberNgto > number and prime(len(s))


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        if check(s):
          print('YES')
        else:
          print("NO")