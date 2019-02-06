def troj(k,w):
    if k==1 or k==w :
        return 1
    else:
        return troj(k-1,w-1)+troj(k,w-1)
    

n=int(input("podaj wysokosc: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(str(troj(j,i)), end="")
    print(" ")
