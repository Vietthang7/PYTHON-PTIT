t = int(input())
while t != 0:
    s = input()
    listDigit = []
    listAlpha = []
    for i in range(len(s)):
        if s[i].isdigit():
            listDigit.append(int(s[i]))
        else:
            listAlpha.append(s[i])
    a = 0
    b = 0
    result = ""
    while a < len(listDigit) and b < len(listAlpha):
        for i in range(listDigit[a]):
            result += listAlpha[b]
        a += 1
        b += 1
    print(result)
    t -= 1
