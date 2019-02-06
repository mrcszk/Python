v1 = 1e9
v2 = 1e-6
for i in range(1000000):
    v1 = v1 + v2
print ('wynik', v1 - 1e9)