if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        result = 0
        for i in range(n - 2):
            l = i + 1
            r = len(a) - 1
            x = a[i]
            while l < r:
                if x + a[l] + a[r] == 0:
                    result += 1
                    l += 1
                elif x + a[l] + a[r] < 0:
                    l += 1
                else:
                    r -= 1
        print(result)
