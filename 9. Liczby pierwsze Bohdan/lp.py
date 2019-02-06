import time
import math
for b in range (20):
    field =int(input("Write range in what you want to work  "))
    listOfPrimeNumbers = []
    startTime=time.time()
    for i in range(field) :
        if i==0 : continue
        numOfIntDivision=0
        sqrt = int(math.sqrt(i+1))
        for a in range(sqrt):
            if((i+1)%(a+1)==0):
                numOfIntDivision+=1
        if  numOfIntDivision<= 1:
            listOfPrimeNumbers.append(i+1)
    print("Your time is %f " % (time.time()-startTime))
    print(listOfPrimeNumbers)