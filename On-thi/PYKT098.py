from sys import *


def check(n):
    for x in n:
        if not x.isdigit():
            return True
        if int(n) >= 10**9:
            return True
        else:
            return False


if __name__ == "__main__":
    f = open("DATA.in", "r")
    res = []
    for line in f:
        x = list(map(str, line.split()))
        for i in x:
            if check(i):
                res.append(i)
    res.sort()
    for x in res:
        print(x, end=" ")
