
for i in range (7):
    for j in range (11):
        if (j==5 and i==3):
            print("x", end = ' ')
        else:
            print ("o",end = ' ')
    print ()
print()
for i in range (7):
    for j in range (11):
        if (j==5-1 or j==5+1) and (i==3-1  or i==3+1) or (j==5 and i==2) or (j==6 and i==3) or (j==4 and i==3) or (j==5 and i==4):
            print("x", end = ' ')
        else:
            print ("o",end = ' ')
    print ()
print()
for i in range (7):
    for j in range (11):
        if ((j==5-2 or j==5+2) and (i==3-2  or i==3+2)) or ((5-1<=j<=5+1 and i==2-1) or (j==6+1 and 3-1<=i<=3+1) or (j==4-1 and 3-1<=i<=3+1) or (5-1<=j<=5+1 and 4+1==i)):
            print("x", end = ' ')
        else:
            print ("o",end = ' ')
    print ()    
print()
for i in range (7):
    for j in range (11):
        if ((j==5-3 or j==5+3) and (i==3-3  or i==3+3)) or ((5-2<=j<=5+2 and i==2-2) or (j==6+2 and 3-2<=i<=3+2) or (j==4-2 and 3-2<=i<=3+2) or (5-2<=j<=5+2 and 4+2==i)):
            print("x", end = ' ')
        else:
            print ("o",end = ' ')
    print () 
print()
a=0
while (a<4):
    for i in range (7):
        for j in range (11):
            if ((j==5-a or j==5+a) and (i==3-a  or i==3+a)) or ((5-(a-1)<=j<=5+(a-1) and i==2-(a-1)) or (j==6+(a-1) and 3-(a-1)<=i<=3+(a-1)) or (j==4-(a-1) and 3-(a-1)<=i<=3+(a-1)) or (5-(a-1)<=j<=5+(a-1) and 4+(a-1)==i)):
                print("x", end = ' ')
            else:
                print ("o",end = ' ')
        print ()  
    print()
    a+=1
