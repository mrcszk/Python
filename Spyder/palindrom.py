napis = input("Podaj napis: ").casefold()

for char in napis:
	if not char.isalpha():
		napis = napis.replace(char,'')

napis2 = napis[::-1]
if napis == napis2:
    print("Palindrom")
else:
    print("Nie palindrom")