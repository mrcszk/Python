def trojkat_pascala(k,w):
   if k==1 or k==w:
     return 1 
   else:
     return trojkat_pascala(k-1,w-1)+trojkat_pascala(k,w-1)
    
n=int(input("podaj wysokosc: "))
for i in range(1,n+1): 
   print ((' ')*(n-i), end=' ')
   for j in range(1,i+1):
       print(str(trojkat_pascala(j,i)), end = ' ')
   print()


