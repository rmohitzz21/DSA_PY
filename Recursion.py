def printN(n):
    if n>0:
        printN(n-1)
        print(n,end = ' ')
# printN(10)

def printRev(n):
    if n>0:
        print(n,end = ' ')
        printRev(n-1)
# printRev(10)

def printOdd(n):
    if n>0:
        printOdd(n-1)
        print(2*n-1,end = ' ')
        
# printOdd(10)

def printEven(n):
    if n>0:
        printEven(n-1)
        print(2*n,end = ' ')
        
# printEven(10)

def printEvenRev(n):
    if n>0:
        print(2*n,end = ' ')
        printEvenRev(n-1)
        
# printEvenRev(10)

def printOddRev(n):
    if n>0:
        print(2*n-1,end = ' ')
        printOddRev(n-1)
        
printOddRev(10)
