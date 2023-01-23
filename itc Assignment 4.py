#question 1
score = input("Enter your score")

score = int(score)

if score < 25:

   print("F")

elif score >= 25 and score < 45:

   print("E")

elif score >= 45 and score < 50:

   print("D")

elif score >= 50 and score < 60:

   print("C")

elif score >= 60 and score < 80:

   print("B")

else:


   print("A")

#question 2
year = int(input("Enter year: "))

if year % 400 == 0 :
    print(year, "is a Leap Year")
elif year % 100 == 0 :
    print(year, "is not a Leap Year")
elif year % 4 == 0 :
    print(year, "is a Leap Year")
else :
    print(year, "is not a Leap Year")

#question 3
from random import randint #to import the randint
mark=0
for i in range(10):
    a=randint(1,20)
    b=randint(1,13)
    que=int(input('Question {}: {} x {} ='.format(i+1,a,b)))
    if que==a*b:
        print('Right!')

    else:
        print('Wrong! The answer is', a*b)

#question 4
x = 200
for i in range(x):
    if i%5==2 and i%6==3 and i%7==2:
        print(i)


