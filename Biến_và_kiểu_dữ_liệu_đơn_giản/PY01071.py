if __name__ == "__main__":
    s = input()
    result = s[-3::]
    if result.lower() == ".py":
        print("yes")
    else:
        print("no")
