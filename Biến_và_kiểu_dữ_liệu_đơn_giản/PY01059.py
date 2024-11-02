if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = input()
        res1, res2 = 0, 1
        check = False
        for i in range(0, len(n)):
            tmp = int(n[i])
            if i & 1 == 1:
                if tmp > 0:
                    res2 *= tmp
                    check = True
            else:
                res1 += int(n[i])
        if check:
            print(str(res1) + " " + str(res2))
        else:
            print(str(res1) + " " + "0")
