if __name__ == "__main__":
    a, k, n = map(int, input().split())
    begin_b = k - a % k
    end_b = n - a
    if begin_b > end_b:
        print(-1)
    else:
        for i in range(begin_b, end_b + 1, k):
            print(i, end=" ")
