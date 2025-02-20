#1.	Write a program to find the largest of two numbers using if-else statements.    

A = 20
B = 30
if A>B :
    print("A is Largest Number")
else :
    print("B is Largest Number")


#2.	Write a program that uses if-else statements to print whether a number is positive, negative, or zero.

P = 25
if P > 0:
    print("The P is Positive")
elif P < 0 :
    print("The P is Negative")
else :
    print("The P is Zero")


#3.	Write a program that checks whether a given number is even or odd using the ternary operator.

G = 22
if G % 2 == 0:
    print("G is Even Number")
else :
    print("G ios Odd Number")

#4.	What is the output of the following expression?
#result = 25 // 4 * 3 + 18 % 7 - 5 * 2 / 2

result = 25 // 4 * 3 + 18 % 7 - 5 * 2 / 2
print("Result:", result)


#5.	Write a program to calculate the area of a triangle given its base and height using the formula Area = (base * height) / 2.

base = 5
height = 10
area = (base * height) / 2
print("Area of the Triangle:", area)


#6.	Write a program to calculate the perimeter of a rectangle using length and width variables.

length = 6
width = 4
perimeter = 2 *(length + width)
print("Perimeter of the Rectangle:",perimeter)


#7.	Write a program that uses the modulus operator (%) to find the remainder when dividing two numbers.

num1 = 27
num2 = 6

remainder = num1 % num2
print("The Remainder is :",remainder)


#8.	Write a program to compare two numbers and print whether the first is greater, smaller, or equal to the second using relational operators.

M = 20
N = 28

if M > N :
    print("M number is greater than the N number")
elif M < N :
    print("M number is smaller than the N number")
else :
    print("Both are equal")


#9.	Write a program that takes two integers and performs both floor division (//) and modulo (%) operations. Print the results

a = 98
b = 77

floor_div = a // b
modulo = a % b

print("Floor Division is :",floor_div)
print("Modulo is :",modulo)


#10.  Write a program that prints the grade based on the score input using if-else statements (A for 90-100, B for 80-89, etc.).

score = 91

if 90 <= score < 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
elif 50 <= score < 60:
    print("Grade: E")
else:
    print("Grade: F (Fail)")