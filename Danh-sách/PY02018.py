if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(1, n + 2):
        if i not in a:
            print(i)
            break
