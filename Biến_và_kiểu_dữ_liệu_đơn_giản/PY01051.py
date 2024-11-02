if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        sumDigit = 0
        for i in range(0, len(s)):
            sumDigit += int(s[i])
        if str(sumDigit) == str(sumDigit)[::-1] and sumDigit > 9:
            print("YES")
        else:
            print("NO")
