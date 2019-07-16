# =============================================================================
# n=20
# for j in range (n):
#     for i in range (j):
#         if (i==1):
#             print ((" "*n)+("!"))
#         elif (i%2==1):
#             print ((" ")*(n-i)+ (" !")+ (" *")*(i-2)+ (" !"))
#         elif (i%2==0):
#             print ((" ")*(n-i),end ='')
#             for j in range (i):
#                 if j==1:
#                     print (' *',end = '')
#                 elif (j+3)%4==0:
#                     print (' o',end = '')
#                 else:
#                     print (' *',end = '')
#             print()
# for i in range (n//4):
#     print (' '*(n -n//4)+ ' *'*(n//4))
# 
# =============================================================================
n=20

for i in range (n):
    if (i==1):
        print (("!").rjust(n))
    elif (i%2==1):
        print (("!").rjust(n-i+1)+ (" *")*(i-2)+ (" !"))
    elif (i%2==0):
        print ((" ").rjust(n-i-1),end='')
        for j in range (i):           
            if (j+3)%4==0 and j!=1:
                print (' o',end = '')
            else:
                print (' *',end = '')
        print()
for i in range (4):
    print (' '*(n -8)+ ' *'*8)
            