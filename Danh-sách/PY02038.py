from sys import *

if __name__ == "__main__":
    s = ""
    for line in stdin:
        a = line.strip().split()
        for x in a:
            s += x + " "
    s = s.lower()
    s = s.replace("?", ".")
    s = s.replace("!", ".")
    s = s.replace(". ", ".")
    s = s.replace(" . ", ".")
    s = s.replace(". ", ".")
    res = s.split(".")
    for x in res:
        # in ra từng câu 1 và in ra chữ cái đầu tiên trong câu
        print(x.capitalize())
