def solve(a, b):
    return a.count(b)


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        k = input()
        print(solve(s, k))
