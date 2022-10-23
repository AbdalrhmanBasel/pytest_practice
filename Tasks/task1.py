"""
Write a calculator with operations + - / *.
First, the user enters 2 numbers line by line,
and then the operation symbol.
The result of the operation is displayed at the end.
"""

num1 = input("First Number: ")
num2 = input("Secound Number: ")
operation = input("Operation: ")


def addition(num1, num2):
    print(num1 + num2)


def subtraction(num1, num2):
    print(num1 - num2)


def division(num1, num2):
    print(num1 / num2)


def multiplication(num1, num2):
    print(num1 * num2)


if operation == "+":
    addition(num1, num2)
elif operation == "-":
    subtraction(num1, num2)
elif operation == "/":
    division(num1, num2)
elif operation == "*":
    multiplication(num1, num2)
else:
    print("Operation is correct!")
