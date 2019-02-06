import os
import time
while True:
    a=0
    while (a<3):
        for i in range (7):
            for j in range (11):
                if ((j==5-a or j==5+a) and (i==3-a  or i==3+a)) or ((5-(a-1)<=j<=5+(a-1) and i==2-(a-1)) or (j==6+(a-1) and 3-(a-1)<=i<=3+(a-1)) or (j==4-(a-1) and 3-(a-1)<=i<=3+(a-1)) or (5-(a-1)<=j<=5+(a-1) and 4+(a-1)==i)):
                    print("x", end = ' ')
                else:
                    print ("o",end = ' ')
            print ()  
        time.sleep(0.3)
        os.system("cls")
   
        a+=1
    while (a>=0):
        for i in range (7):
            for j in range (11):
                if ((j==5-a or j==5+a) and (i==3-a  or i==3+a)) or ((5-(a-1)<=j<=5+(a-1) and i==2-(a-1)) or (j==6+(a-1) and 3-(a-1)<=i<=3+(a-1)) or (j==4-(a-1) and 3-(a-1)<=i<=3+(a-1)) or (5-(a-1)<=j<=5+(a-1) and 4+(a-1)==i)):
                    print("x", end = ' ')
                else:
                    print ("o",end = ' ')
            print ()  
        time.sleep(0.3)
        os.system("cls")
        a-=1