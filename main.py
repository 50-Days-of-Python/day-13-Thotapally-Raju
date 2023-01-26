import math

a=int(input())

b=int(input()) 

if(a>0 and b>0):

 print(math.ceil((a+(a*b)/100)))

else:

 print ("Invalid Input")
