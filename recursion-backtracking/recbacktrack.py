def printnum(n):
    if n==0:
        return n
    printnum(n-1)
    print(n)


if __name__ == "__main__":
    printnum(5)