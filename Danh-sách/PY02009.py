if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        CountMax, value = 0, 0
        cnt = [0] * 1001
        for i in range(n):
            x = int(input())
            cnt[x] += 1
            if cnt[x] > CountMax:
                CountMax = cnt[x]
                value = x
            elif cnt[x] == CountMax:
                if x < value:
                    value = x
        print(value)
