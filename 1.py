no=0
a=int(input("enter a three digit number:"))
while(a>0):
  dig=a%10
  no=no+1
  a=a//10
print("number of given digits is:",no)