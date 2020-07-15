def fib(n):
    if n>=2:
        return fib(n-1) + fib(n-2)
    elif(n==1):
        return 1
    else:
        return 0

for i in range (20):
    print(fib (i), end =",")