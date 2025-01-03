from math import *


def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def primeDigit(n):
    sum = 0
    while n != 0:
        tmp = n % 10
        if tmp != 2 and tmp != 3 and tmp != 5 and tmp != 7:
            return False
        sum += tmp
        n //= 10
    return prime(sum)


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = input()
        r = n[::-1]
        if prime(int(n)) and prime(int(r)) and primeDigit(int(n)):
            print("Yes")
        else:
            print("No")
