def Try(s, l, a, b, c, result):
    if len(s) == l:
        if a <= b and b <= c and a > 0:
            result.append(s)
        return
    if len(s) < l:
        Try(s + "A", l, a + 1, b, c, result)
        Try(s + "B", l, a, b + 1, c, result)
        Try(s + "C", l, a, b, c + 1, result)


if __name__ == "__main__":
    n = int(input())
    result = []
    for i in range(3, n + 1):
        Try("", i, 0, 0, 0, result)
    result.sort(key=lambda s: (len(s), s))
    for x in result:
        print(x)
