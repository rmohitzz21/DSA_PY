# calculate sum of first N natural Number

def sumN(n):
    if n==1:
        return 1
    return n + sumN(n-1)
# print("Sum is ", sumN(10))

# write a function to calculate first N odd natural number

def sumNOdd(n):
    if n==1:
        return 1
    return 2*n-1 + sumNOdd(n-1)
print("Sum is ", sumNOdd(3))  # 1 3 5 

# write a function to calculate first N Even natural number

def sumNEven(n):
    if n==1:
        return 2
    return 2*n + sumNEven(n-1)
print("Sum is ", sumNEven(3))  # 2 4 6 

# cal product of N number Fact

def fact(n):
    if n==0:
        return 1
    return n * favt(n-1)
print("Sum is ", sumNEven(3)) 

# calculate sum of square  

def sumNsquare(n):
    if n==1:
        return 1
    return n*n + sumNsquare(n-1)
print("Sum is ",sumNsquare(4)) # 1 4 9 16