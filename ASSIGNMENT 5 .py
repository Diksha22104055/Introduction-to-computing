# question 1
string = input("enter your string")
print(string[::-1])

# question 2
hey = int(input("enter a range"))
divisible_by = int(input("enter number for divisibility test"))
for i in range(1, hey + 1):
    if i % divisible_by == 0:
        print(i)

# question 3
import math
a = float(input("enter your first length"))
b = float(input("enter your second length"))
c = float(input("enter your third length"))
if a > b + c or b > a + c or c > a + c:
    triangle = False
    print("triangle cannot be formed")
else:
    triangle = True
    print("triangle can be formed")
if triangle == True:
    semi_perimeter = (a + b + c)/2
    x = semi_perimeter - a
    y = semi_perimeter - b
    z = semi_perimeter - c
    area = math.sqrt(semi_perimeter*x*y*z)
    print(area)
else:
    print("triangle not formed, area does not exist")

# question 4
a = int(input("number of max stars in a line"))
x = 0
while x != a:
    print(x*" * ")
    x += 1
while a != 0:
    print(a*" * ")
    a -= 1

#question 5
char = 65
n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
  for j in range(i):
    print(chr(char), end="")
    char += 1
    if char > 90:
      char = 65
  print()

# question 6
upper_value = int(input("enter range"))
print("Prime Numbers in the range", upper_value, "are: ")
for number in range(2, upper_value + 1):
    for i in range(2, number):
        if (number % i) == 0:
            break
    else:
        print(number)

# question 7
x = int(input("enter range"))
for i in range(1, x+1):
    if i % 7 == 0 and i % 11 == 0:
        print(i)

# question 8
initial = []
even = []
odd = []
positive = []
negative = []

while True:
    num = input("enter num")
    if num == '':
        break
    else:
        initial.append(num)
a = 0
while a in range(0, len(initial)):
    if int(initial[a]) % 2 == 0 and int(initial[a]) > 0:
        even.append(initial[a])
        a += 1
    elif int(initial[a]) % 2 != 0 and int(initial[a]) > 0:
        odd.append(initial[a])
        a += 1
    else:
        a += 1
t = 0
while t in range(0, len(initial)):
    if int(initial[t]) < 0:
        negative.append(initial[t])
        t += 1
    else:
        positive.append(initial[t])
        t += 1
h = 0
new = [*set(initial)]
while h < len(new):
    g = new[h]
    p = initial.count(g)
    print(g, "appears", p, "times")
    h += 1

print("even numbers are:-", even)
print("odd numbers are:-", odd)
print("positive numbers are:-", positive)
print("negative numbers are:-", negative)

# question 9
string = input("enter your string")
new_string = string.split()
new_new_string = [*set(new_string)]
h = 0
while h < len(new_new_string):
    g = new_new_string[h]
    p = new_string.count(g)
    print(g, "appears", p, "times")
    h += 1




