nazwy_miesiecy = ['styczen','luty','marzec','kwiecien','maj','czerwiec','lipiec','sierpien','wrzesien','pazdziernik','listopad','grudzien']
miesiace = [31,28,31,30,31,30,31,31,30,31,30,31]
dzien_tygodnia = 1 #dzien tygodnia, 1 znaczy poniedzialek, 5 piatek, 7 niedziela
dzien = 1 #nr dnia w miesiacu
ile = 0

print("Piątki trzynastego w latach 2001-2014")
for i in range(2001,2015):
    print("Rok: " + str(i))
    miesiace[1] = 28
    if i % 4 == 0:#gdy rok przestepny
        miesiace[1] = 29
    ob_miesiac = 0;
    while ob_miesiac < 12:
        dzien += 1
        dzien_tygodnia += 1
        if dzien > miesiace[ob_miesiac]:
            dzien = 1
            ob_miesiac += 1
        if dzien_tygodnia > 7:
            dzien_tygodnia = 1
        if dzien == 13 and dzien_tygodnia == 5:
            print(nazwy_miesiecy[ob_miesiac])
            ile += 1
print("Piątek trzynastego wystąpił: " + str(ile) + " razy")