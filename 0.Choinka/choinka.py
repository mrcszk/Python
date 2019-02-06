for i in range (10):
    print ((" ")*(10-i), (" *")*i)
for i in range (10):
    if (i==1):
        print ((" "*10), (" !"))
    elif (i%2==1):
        print ((" ")*(11-i), (" !"), ("*"),(" *")*(i-3), ("!"))
   # elif(i%4==2):
    #    print((" ") * (10 - i), (" *")*2, (" *")*i)
    else:
        print((" ") * (10 - i),(""), (" *") *i)