x = int(input("Podaj wspolrzedne x"))
y = int(input("Podaj wspolrzedne y"))


if (x>0):
  if (y>0):
    print ("Jest to I cwiartka")
  elif (y==0):
    print ("Punkt nalezy do OX.")
  else:
    print ("Jest to IV cwiartka.")
elif (x == 0):
  if (y>0 or y<0):
    print ("Punkt nalezy do OY.")
  else:
    print ("Punkt nalezy jednoczesnie do OX i do OY.")
elif (x < 0):
  if (y>0):
    print ("Jest to II cwiartka")
  elif (y==0):
    print ("Punkt nalezy do OX.")
  else:
    print ("Jest to III cwiartka.")
