def tn(s):
    l, r = 0, len(s) - 1
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def even(s):
    for i in range(len(s)):
        if int(s[i]) % 2 != 0:
            return False
    return True


def sumDigit(n):
    s = str(n)
    return len(s) % 2 == 0 and tn(s) and even(s)


if __name__ == "__main__":
    t = int(input())
    while t != 0:
      n = int(input())
      for i in range(22,n,2):
        if sumDigit(i):
          print(i,end=" ")
      print()
      t -= 1
