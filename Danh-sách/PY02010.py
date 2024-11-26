if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        a = []
        for j in range(n):
            a.append(int(input()))
        if max(a) == min(a):
            print("BANG NHAU")
        else:
            print(min(a), max(a))
        a.clear()
