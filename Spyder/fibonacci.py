def fib_rek(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rek(n-2)+fib_rek(n-1)
        
print("Rekurencyjnie:")
print(fib_rek(0))
print(fib_rek(1))
print(fib_rek(2))
print(fib_rek(3))
print(fib_rek(5))
print(fib_rek(7))
print(fib_rek(13))

def fib_iter(n):
    if n==0:
        return 0
    elif n < 2:
        return 1
    else:
        f1=f2=1
        for i in range(2,n):
            tmp = f1 + f2
            f1 = f2
            f2 = tmp
        return f2
            
print("Iteracyjnie:")
print(fib_iter(0))
print(fib_iter(1))
print(fib_iter(2))
print(fib_iter(3))
print(fib_iter(5))
print(fib_iter(7))
print(fib_iter(13))