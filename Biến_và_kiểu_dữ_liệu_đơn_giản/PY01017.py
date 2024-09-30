t = int(input())
while t != 0:
    s = input()
    result = ""
    cnt = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            result += str(cnt) + s[i - 1]
            cnt = 1

    result += str(cnt) + s[len(s) - 1]
    print(result)
    t -= 1
