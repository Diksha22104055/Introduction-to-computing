#q1
''' #Write a Python program to count the number of occurrences of each word or
character in the string entered by the user.'''

A=input("enter a word")
count_of_letters=len(A.split())
characters=len(A)
if (count_of_letters > 1):
    len(A.split())
    print(count_of_letters)
else:print(characters)

#q2 Write a python script to print next date of input date.
year = int(input("Input a year: "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))


#q3
n=int(input('enter a number'))
listoftuples = [n]
thelistoftuples = [(n , n**2)]
print(thelistoftuples)


#q4
a = {4:['D','Poor'], 5:('C','Below Average'), 6:('C+','Average'), 7:('B','Good'), 8:('B+','Very Good'), 9:('A','Excellent'), 10:('A+','Outstanding')}

grade = int(input('Grade : '))
if grade >= 4 and grade <= 10:
    print('Your Grade is',a[grade][0], 'and', a[grade][1], 'Performance.')
else: raise ValueError("Grade invalid")

#q5
for i in range(10, 0, -1):
    for j in range(11-i):
        print(" ", end="")
    for k in range(i):
        print(chr(65+k),end=" ")
    print()

#question 6

repeat="Y"
dic={}
dic2={}

liste=["Y","y","n","N"]
while repeat=="Y" or repeat=="y":
    name = str(input("Enter student name : "))
    sid = int(input("Enter student SID : "))
    if sid<0:
        print("\nError\nSID can't be negative\n")
    else:
        dic.update({sid: name})
        dic2.update({name:sid})
        repeat = str(input("Enter Y to continue or N to end : "))
    if repeat=="N" or repeat=="n":
        break
    elif (not (repeat in liste)):
        print("\nError\nPlease enter valid input['Y' or 'N']")
        repeat=str(input("\nEnter Y to continue or N to end : "))
#question 6 (part a)

print("\nQ.6(a)")
print("The Dictionary containing {'SID':'Name'} is shown below")
print(dic)
# b

print("\nQ.6(b)")
list_k=sorted(dic2)
dic3={}
for ele in list_k:
    dic3.update({dic2.get(ele):ele})
print("The Dictionary after sorting according to name : ")
print(dic3)
# c

print("\nQ.6(c)")
sort_dic = sorted(dic)
dic4 = {}
for va in sort_dic:
    dic4.update({va: dic.get(va)})
print("The Dictionary after sorting according to SID : ")
print(dic4)
# d
print("\nQ.6(d)")

enter_sid = int(input("Enter SID to get name of student : "))

output_name = str(dic.get(enter_sid))

print(f"Name of student with SID {enter_sid} is {output_name}.")


#q7

n = int(input("Enter number of elements N in fibonacci series:\n[N must be positive Integer]: N="))

if n <= 0:
    print("\nError\nNumber of elements in fibonacci series must be integer and greater than zero.")

else:

    if n == 1:
        print("\nThe fibonacci series with 1 element is shown below\n[1]")
        print("\nAverage of given fibonacci series is", 1)

    elif n == 2:
        print("\nThe fibonacci series with 2 element is shown below\n[1,1]")
        print("\nAverage of given fibonacci series is", 1)

    else:

        list1 = [1, 1]

        a = 1
        b = 1

        for i in range(n - 2):
            s = a + b
            list1.append(s)
            a = b
            b = s

        print(f"\nThe fibonacci series with {n} elements is shown below:")
        print(list1)

        sum = 0  # intial sum=0

        for num in list1:
            sum = sum + num
        average = (sum / n)

        two_decimal = "{:.2f}".format(average)

        print(f"\nAverage of given fibonacci series is {two_decimal}")



#question8

Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}


#question8 (part a)
A = Set1^Set2
print(A)

#question 8(part b)
B = (Set1|Set2|Set3) - ((Set1&Set2) | (Set2&Set3) | (Set3&Set1))
print(B)

#question 8 part (c)
C = (Set1&Set2) | (Set2&Set3) | (Set3&Set1)
print(C)

#question8 (part d)
D = set()
for i in range (1,11) :
    if i not in Set1:  D.add(i)
print(D)

# question8 (part e)
E = set()
for i in range (1,11) :
    if i not in Set1|Set2|Set3:
        #print(i)
        E.add(i)
print(E)






