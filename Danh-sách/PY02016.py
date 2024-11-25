if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        d = dict()
        a = list(map(int, input().split()))
        for x in a:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        ok = False
        for x in d:
            if d[x] > n // 2:
                print(x)
                ok = True
                break
        if ok == False:
            print("NO")
