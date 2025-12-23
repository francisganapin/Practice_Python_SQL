def printNos(n):
    if n == 0:
        return 
    print(n,end="")
    printNos(n -1 )


printNos(20)