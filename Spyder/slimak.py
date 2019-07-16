h=float(input("Podaj h:"))
x=4
y=3
z=5
s=0
l=0
def ile(x,y,z,h):
    s=0
    l=1
    while True:    
        s+=x
        if s>=h:
            break
        k=s//z
        if s-y<=k*z:
            s=k*z
        else:
            s-=y
        l+=1
    return l

print (ile(x,y,z,h))
    