dlugosc = int(input("Podaj dlugosc preta: "))

pret=[0]*11
pret[1]=1
pret[2]=5
pret[3]=8
pret[4]=9
pret[5]=10
pret[6]=16
pret[7]=17
pret[8]=20
pret[9]=24
pret[10]=26
a = pret [dlugosc]
b=0
c=0
for i in range (dlugosc):
    if (a<(pret[i]+pret[dlugosc-i])):
        a=pret[i]+pret[dlugosc-i]
        b=i
    elif (a==(pret[i]+pret[dlugosc-i])):
        c=i
if b==c or b==dlugosc-c:
    print ("Maksymalny zysk",a,"Trzeba podzielic na kawalki: ",b, "i",dlugosc-b)
else:
    print ("Maksymalny zysk",a,"Trzeba podzielic na kawalki:",b,"i", dlugosc-b,"lub",c,"i",dlugosc-c) 