if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        res = 1
        n = input()
        for j in n:
            tmp = ord(j) - ord("0")
            if tmp > 0:
                res *= tmp
        print(res)
