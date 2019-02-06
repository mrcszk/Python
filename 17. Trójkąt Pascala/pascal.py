def wyswietlanie(wiersz):
    print(' '.join([str(i) for i in wiersz]).center(50))

x = int(input("Podaj liczbe wierszy: "))
wiersz = [1]
wyswietlanie(wiersz)
for i in range(x - 1):
    kolejny_wiersz = [1]
    for j in range(len(wiersz) - 1):
        kolejny_wiersz.append(wiersz[j] + wiersz[j + 1])
    kolejny_wiersz.append(1)
    wiersz = kolejny_wiersz
    wyswietlanie(wiersz)