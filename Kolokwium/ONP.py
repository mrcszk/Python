class Node:
  def __init__(self,data):
    self.data=data
    self.prev=None 
  def __str__(self):
    return str(self.data) 
class Stos:
  def __init__(self):
    self.top=None 
  def push(self,data):
    n=self.top
    new=Node(data)
    new.prev=n
    self.top=new 
  def pop(self):
    n=self.top.data
    self.top=self.top.prev
    return n 
  def isEmpty(self):
    if self.top==None:
      return True
    else:
      return False 
stos=Stos()     
wyrazenie=input("Wpisz(oddziel spacja): ")
tmp=''
for i in range(0,len(wyrazenie)):
  if wyrazenie[i].isdigit():
    tmp+=wyrazenie[i] 
  if wyrazenie[i]==' ':
    stos.push(int(tmp))
    tmp="" 
  if wyrazenie[i]=='+':
    a=stos.pop()
    b=stos.pop()
    stos.push(a+b)
  if wyrazenie[i]=='-':
    a=stos.pop()
    b=stos.pop()
    stos.push(a-b)
  if wyrazenie[i]=='*':
    a=stos.pop()
    b=stos.pop()
    stos.push(a*b)
  if wyrazenie[i]=='/':
    a=stos.pop()
    b=stos.pop()
    stos.push(a/b)    
print(stos.pop())
