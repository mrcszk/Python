import time

counter = 0
squareCounter = 0
grow = True

print("Podaj nieparzysta liczbe kolumn: ", end="")
cols = int(input())
print("Podaj nieparzysta liczbe wierszy: ", end="")
rows = int(input())

if (rows<cols):
    radius = int((rows/2))
else:
    radius = int((cols/2))
    
centerRow = int(rows/2) + 1
centerCol = int(cols/2) + 1

while (counter<=20):
    for x in range(1,rows+1):
        for y in range(1,cols+1):
            if ( x == (centerRow-(squareCounter % (radius+1))) or x == (centerRow+(squareCounter % (radius+1))) ) and y <= (centerCol+(squareCounter%(radius+1))) and y >= (centerCol-(squareCounter%(radius+1))):
                print("X", end=" ")
            elif( y == (centerCol-(squareCounter % (radius+1))) or y == (centerCol+(squareCounter % (radius+1))) ) and x <= (centerRow+(squareCounter%(radius+1))) and x >= (centerRow-(squareCounter%(radius+1))):
                print("X", end= " ")
            else:
                print("O", end=" ")
        else:
            print("")
    else:
        print("")
    if grow:
        squareCounter += 1
        if squareCounter == radius:
            grow = False
    else:
        squareCounter -= 1
        if squareCounter == 0:
            grow = True
    counter += 1
    time.sleep(0.5)