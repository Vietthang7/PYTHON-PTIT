def check(s):
    for i in s:
        if i not in ["0", "1", "2"]:
            return False
    return True


if __name__ == "__main__":
    t = int(input())
    while t != 0:
        t -= 1
        s = input()
        if check(s):
            print("YES")
        else:
            print("NO")
