t = int(input())
while t != 0:
    s = input()
    ok = 1
    for i in range(1, len(s)):
        if s[i] < s[i - 1]:
            print("NO")
            ok = 0
            break
    if ok:
        print("YES")
    t -= 1
