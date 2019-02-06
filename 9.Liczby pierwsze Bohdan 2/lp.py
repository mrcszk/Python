import time
import math

for a in range(20):
    field = int(input("Write range in what you want to work  "))
    listOfPrimeNumbers = []
    i = 2
    startTime = time.time()
    while i < field:
        a = 1
        numOfIntDivision = 0
        sqrt = int(math.sqrt(i))
        while a <= sqrt:
            if ((i) % (a) == 0):
                numOfIntDivision += 1
            a += 1
        if numOfIntDivision <= 1:
            listOfPrimeNumbers.append(i)
        i += 1
    print("Your time is %f " % (time.time() - startTime))
    print(listOfPrimeNumbers)
