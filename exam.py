# 1. Write a Python program to print 'Hello Python' and
# 'Welcome to Programming' on two separate lines.

print("Hello Python")
print("Welcome to Programming")

# 2. Write a Python program to take the user's
# name as input and print: Welcome, <name>.

name = input("Enter your name: ")
print("Welcome,", name)

# 3. Write a Python program to take two numbers as input and print their sum.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2
print("Sum =", sum)

# 4. Write a Python program to take a number as input and check whether it is even or odd.

num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
    
# 5. Write a Python program to take a number as input and check whether it is positive, negative, or zero.

num = int(input("Enter number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 6. Write a Python program using a for loop to print the numbers from 1 to 10.

for i in range(1, 11):
    print(i)
    
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)

i = 1

while i <= 10:
    print(i)
    i = i + 1
    
# 7. Given fruits = ['Apple', 'Mango', 'Banana', 'Orange'], write a Python program to print each item using a for loop.

fruits = ['Apple', 'Mango', 'Banana', 'Orange']

for fruit in fruits:
    print(fruit)    
    
