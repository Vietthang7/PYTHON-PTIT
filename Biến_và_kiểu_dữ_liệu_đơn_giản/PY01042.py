def check(s):
    for i in s:
        if i not in ['1', '2', '0']:
            return False
    return True


if __name__ == "__main__":
    t = int(input())
    while t != 0:
        s = input()
        if check(s):
            print("YES")
        else:
            print("NO")
        t -= 1
