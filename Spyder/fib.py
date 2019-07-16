# =============================================================================
# def fib(n):
#     if result[n] !=-1:
#         return result[n]
#     if n>=2:
#          result[n] = fib(n-1) + fib(n-2)
#          return result[n]
#     elif(n==1):
#         result[1]=1
#         return result[1]
#     else:
#         result[0]=0
#         return result[0]
# result = [-1]*21
# 
# fib(20)
# for i in range (20):
#     print(result[i], end =",")
# print()
#     
# =============================================================================

# Programowanie dynamiczne wstępujące, wersja z listą.
def fibonacci(n):
    F = [0] + n * [1]   # trzymamy wszystkie wartości
    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]
    return F
n=10
A = fibonacci(n)
for i in range(n):
    print(A[i], end =', ')