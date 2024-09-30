if __name__ == "__main__":
    s = input()
    dem_Upper = 0
    for i in range(len(s)):
        if s[i].isupper():
            dem_Upper += 1

    lower_char = len(s) - dem_Upper
    if lower_char >= dem_Upper:
        print(s.lower())
    else:
        print(s.upper())