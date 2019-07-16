# =============================================================================
# dlugosc = int(input("Podaj dlugosc preta: "))
# 
# pret=[0]*11
# 
# pret[1]=1
# pret[2]=5
# pret[3]=8
# pret[4]=9
# pret[5]=10
# pret[6]=16
# pret[7]=17
# pret[8]=20
# pret[9]=24
# pret[10]=26
# a = pret [dlugosc]
# b=0
# c=0
# d=0
# e=0
# for i in range (dlugosc+1):
#     for j in range (dlugosc+1):
#         if (a<(pret[i]+pret[j]+pret[dlugosc-i-j])and dlugosc-i-j>=0 and j<=i):
#             a=pret[i]+pret[j]+pret[dlugosc-i-j]
#             b=i
#             d=j
#         elif (a==(pret[i]+pret[j]+pret[dlugosc-i-j])and dlugosc-i-j>=0 and j<=i):
#             c=i
#             e=j
# if b==c or b==dlugosc-c:
#     print ("Maksymalny zysk",a,"Trzeba podzielic na kawalki: ",b, "i",dlugosc-b)
# elif c==0 or b==dlugosc-c-e :
#     print ("Maksymalny zysk",a,"Trzeba podzielic na kawalki:",b,",", d,"i",dlugosc-b-d) 
# elif (dlugosc-c-e!=0 or dlugosc-b-d!=0):
#     print ("Maksymalny zysk",a,"Trzeba podzielic na kawalki:",b,",",d,"i",dlugosc-b-d,"lub",c,",",e,"i",dlugosc-c-e)
# 
# 
# elif dlugosc-c-e==0 and dlugosc-b-d==0 :
#     print ("Maksymalny zysk",a,"Trzeba podzielic na kawalki:",b,"i", dlugosc-b,"lub",c,"i",dlugosc-c) 
# 
# =============================================================================
# A Dynamic Programming solution for Rod cutting problem 
INT_MIN = -32767
  
# Returns the best obtainable price for a rod of length n and 
# price[] as prices of different pieces 
def cutRod(price, n):
    val = []
    for i in range(n+1):
        val.extend([0,[]])
    output = list()
    for i in range(1, n+1):
        max_val = 0
        cur_max_index = -1
        for j in range(i):
            cur_val = price[j] + val[2*(i-j-1)]
            if(cur_val>=max_val):
                max_val = cur_val #store current max
                cur_max_index = j #and index
        a= i- cur_max_index -1
        val[2*i+1].extend(val[2*a+1]) 
        val[2*i+1].append(i-a) 
        if cur_max_index != -1:
            output.append(cur_max_index) #append in output index list
        val[2*i] = max_val
    print(val) #print array
    return val[2*n]

# Driver program to test above functions 
arr = [1, 5, 8, 9, 10, 16, 17, 20, 24, 26] 
size = len(arr) 
print("Maximum Obtainable Value is " + str(cutRod(arr, size))) 
