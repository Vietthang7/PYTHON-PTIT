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
        ngto = 0
        noNgto = 0
        for i in range(len(s)):
            if s[i] in ["2", "3", "5", "7"]:
                ngto += 1
            else:
                noNgto += 1
        if prime(len(s)) and ngto > noNgto:
            print("YES")
        else:
            print("NO")
