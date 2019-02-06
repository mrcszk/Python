a=1
b=a
c=a+b
for i in range (5):
    print(a, end =",")
    print(b, end =",")
    print(c, end =",")
    a=c+b
    b=a+c
    c=a+b