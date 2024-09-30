def solve(s):
    for i in range(len(s)):
        if s[i] != "4" and s[i] != "7":
            return "NO"
    return "YES"


if __name__ == "__main__":
    t = int(input())
    while t != 0:
        s = input()
        print(solve(s))
        t -= 1

