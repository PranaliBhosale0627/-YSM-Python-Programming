# 1. Write a function greet(name) that takes a name ehich is store in variable as input and prints "Hello, [name]!".

def greet(name):
    print("Hello,", name,"!")

greet("John")
print("-------------")


# 2. Create a function square(num) that returns the square of a given number.

def square(num):
    return num ** 2

print(square(55))
print("-------------")

# 3. Write a function is_even(n) that returns True if a number is even, otherwise False.

def is_even(n):
    return n % 2 == 0

print(is_even(56))
print("-------------")

# 4. Define a function sum_numbers(a, b=10) that takes two numbers and returns their sum. If the second number is not provided, it should default to 10.

def sum_numbers(a, b=10):
    return a + b

print(sum_numbers(5))
print(sum_numbers(5,33))
print("-------------")

# 5. Write a recursive function factorial(n) to calculate the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))
print("-------------")

# 6. Use a lambda function with filter( ) to get all even numbers from a list: [1, 2, 3, 4, 5, 6, 7, 8].

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
print("-------------")

# 7. Write a while loop to print the first 5 multiples of 3.

count = 1
while count <= 5:
    print(count * 3) 
    count += 1
print("-------------")

# 8. Create a loop that prints all numbers from 1 to 20 but skips multiples of 5.

for i in range(1, 21):
    if i % 5 == 0:
        continue
    print(i)
print("-------------")

# 9. Write a loop that stops when it encounters the number 7 in this list: [1, 2, 3, 4, 5, 6, 7, 8, 9].

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in num_list:
    if num == 7:
        break 
    print(num)
print("----------------------")

# 10. Write a program that checks if a year is a leap year. (Hint: A year is a leap year if it is divisible by 4 but not by 100, except when it is also divisible by 400.)  

def is_leap_year(year):

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = 2025
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
print("----------------------")