t = int(input())
while t != 0:
    s = input()
    rev = s[::-1]
    if len(s) <= 1:
        print("YES")
        continue
    a = 1
    b = 1
    result = True
    while a < len(s) and b < len(rev):
        if abs(ord(s[a]) - ord(s[a - 1])) != abs(ord(rev[b]) - ord(rev[b - 1])):
            result = False
            break
        a += 1
        b += 1
    if result:
        print("YES")
    else:
        print("NO")
    t -= 1
