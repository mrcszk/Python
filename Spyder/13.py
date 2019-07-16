nazwy_miesiecy=['styczen','luty','marzec','kwiecien','maj','czerwiec','lipiec','sierpien','wrzesien','pazdziernik','listopad','grudzien']
ilosc_dni_miesiaca=[31,28,31,30,31,30,31,31,30,31,30,31]
dzien_miesiaca=1 
dzien_tygodnia=1
ile=0 

print("Piatki 13tego w latach 2001-2014")
for i in range(2001,2015):
  print("rok: "+str(i))
  ilosc_dni_miesiaca[1]=28
  if i%4==0:
    ilosc_dni_miesiaca[1]=29
  ob_miesiac=0
  while ob_miesiac<12:
    dzien_miesiaca+=1
    dzien_tygodnia+=1
    if dzien_miesiaca > ilosc_dni_miesiaca[ob_miesiac]:
      dzien_miesiaca=1 
      ob_miesiac+=1 
    if dzien_tygodnia>7:
      dzien_tygodnia=1 
    if dzien_miesiaca==13 and dzien_tygodnia==5:
      print(nazwy_miesiecy[ob_miesiac])
      ile+=1
print("Piatek 13tego wystapil "+str(ile)+" razy")