#QUESTION 1
def is_perfect():
    num = int(input("Enter a number: "))
    divisors = [i for i in range(1, num) if num % i == 0]
    if sum(divisors) == num:
        print(num," is a perfect number.")
    else:
        print(num," is not a perfect number.")

is_perfect()

#QUESTION 2
def is_palindrome():
    string = input("Enter a string: ")
    if string == string[::-1]:
        print(string," is a palindrome.")
    else:
        print(string," is not a palindrome.")

is_palindrome()

#QUESTION 3
def pascal_triangle(n):
    for i in range(n):
        row = [1]
        for j in range(1, i + 1):
            row.append(row[j - 1] * (i - j + 1) // j)
        print(' '.join(str(x) for x in row))

n = int(input("Enter the number of rows: "))
pascal_triangle(n)

#QUESTION 4
def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    sentence = sentence.lower().replace(" ","")
    return set(sentence).issuperset(alphabet)

sentence = input("Enter a sentence: ")
if(is_pangram(sentence) == True):
    print(sentence," is a pangram.")
else:
    print(sentence," is not a pangram.")

#QUESTION 5
def sort_sequence(sequence):
    words = sequence.split("-")
    words.sort()
    sorted_sequence = "-".join(words)
    print(sorted_sequence)

sequence = input("Enter a hyphen-separated sequence of words: ")
sort_sequence(sequence)

#QUESTION 6
class Student:
    pass
class Marks:
    pass
student_1 = Student()
student_2 = Student()
marks_1 = Marks()
marks_2 = Marks()
print(isinstance(student_1, Student))
print(isinstance(student_2, Student))
print(isinstance(marks_1, Marks))
print(isinstance(marks_2, Marks))
print(issubclass(Student, object))
print(issubclass(Marks, object))


#QUESTION 7
class Student:
    pass
class Marks:
    pass
student_1 = Student()
student_2 = Student()
marks_1 = Marks()
marks_2 = Marks()
print(isinstance(student_1, Student))
print(isinstance(student_2, Student))
print(isinstance(marks_1, Marks))
print(isinstance(marks_2, Marks))
print(issubclass(Student, object))
print(issubclass(Marks, object))

#QUESTION 8
class SumToZero:
    def __init__(self, arr):
        self.arr = arr

    def find_triplets(self):
        triplets = []
        arr = self.arr
        arr.sort()
        n = len(arr)
        for i in range(n-2):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                s = arr[i] + arr[l] + arr[r]
                if s == 0:
                    triplets.append([arr[i], arr[l], arr[r]])
                    l += 1
                    r -= 1
                    while l < r and arr[l] == arr[l-1]:
                        l += 1
                    while l < r and arr[r] == arr[r+1]:
                        r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return triplets

arr = [-25, -10, -7, -3, 2, 4, 8, 10]
print(SumToZero(arr).find_triplets())


#QUESTION 9
class ParenthesesChecker:
    def __init__(self):
        pass

    def check_validity(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack:
                    return False
                if char == ")" and stack[-1] != "(":
                    return False
                if char == "]" and stack[-1] != "[":
                    return False
                if char == "}" and stack[-1] != "{":
                    return False
                stack.pop()
        return not stack


p = ParenthesesChecker()
s = input("Enter a string of parentheses to check its validity: ")
print(p.check_validity(s))



