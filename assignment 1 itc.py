#q1
a=int(input("first number"))
b=int(input("second number"))
c=int(input("third number"))
d=(a+b+c)/3
print(d)

#q2
a = float(input("enter your income"))
b = a-10000
c = int(input("dependents"))
d = c*3000
e = b-d
f = (0.2*e)
print(f)

#q3
from math import *
a = float(input("enter value"))
b = a/60
c = (a%60)
d = "mins"
e = floor(b)
f = "secs"
print(e,str(d),"and",c,str(f))

#q4
a = int(input("num1"))
b = float(input("num2"))
c = input("num3")
d = a+b+int(c)
print(d)

#q5
import math
a=0
while a<=345:
    print(math.sin(math.radians(a)), math.cos(math.radians(a)))
    a = a+15
