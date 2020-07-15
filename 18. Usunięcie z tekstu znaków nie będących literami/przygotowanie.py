'''zdanie = input("Podaj zdanie:")
znaki = ["1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","-","+","=",",",".",":",":"]

for i in zdanie:
    if i in znaki:
        zdanie = zdanie.replace(i, "")

print(zdanie.lower())'''

zdanie = input("Podaj zdanie:")
zdanie.lower()
for i in zdanie:
    if (ord(i)>122 or ord(i)<97):
        zdanie = zdanie.replace(i, "")

print(zdanie)