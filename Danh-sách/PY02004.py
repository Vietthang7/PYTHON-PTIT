if __name__ == "__main__":
    n = int(input())
    result = 0
    a = list(map(int, input().split()))
    for i in range(1, n):
        if a[i] != a[i - 1]:
            result += 1
    print(result)
