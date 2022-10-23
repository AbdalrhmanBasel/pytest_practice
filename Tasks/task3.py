"""
History calculator.
The calculator should work in the REPL format: we enter a value,
the result is calculated and displayed on the screen, the program again prompts you
to enter a value. After each operation, a list with a history of previously
performed operations should be displayed.
"""

import time

history =[]


def timer():
    time.sleep(1)
    print("")
    print("--------------------------------------------------------------------------")


def add(num1, num2):
    sum = str(num1 + num2)
    print("")
    print("The sum is " + sum)

    history.append(sum)
    timer()


def minus(num1, num2):
    diff = str(num1 - num2)
    print("")
    print("The difference is " + diff)

    history.append(diff)
    timer()


def multiply(num1, num2):
    product = str(num1 * num2)
    print("")
    print("The product is " + product)

    history.append(product)
    timer()


def divide(num1, num2):
    div = str(num1 / num2)
    print("")
    print("The division is " + div)

    history.append(div)
    timer()


def view_history():
    print(history)
    timer()


def lastResult(user_input2, num):
        last_result = history[-1]
        print(last_result)
        if user_input2 == '+':
            add(float(last_result), num)
        elif user_input2 == '-':
            minus(float(last_result), num)
        elif user_input2 == '*':
            multiply(float(last_result), num)
        elif user_input2 == '/':
            divide(float(last_result), num)
        else:
            print("Unknown input!")


print("Enter '+' for addition:")
print("Enter '-' for subtraction:")
print("Enter '*' for multiplication:")
print("Enter '/' for division:")
print("Enter 'h' to check history:")
print("Enter 'lr' to make calculation with last result:")
print("Enter 'quit' to end the calculator:")

while True:

    user_input = input("OPERATION: ")

    if user_input == 'quit':
        break
    elif user_input == '+':
        num1 = float(input("enter 1st number: "))
        num2 = float(input("enter 2nd number: "))
        add(num1, num2)
    elif user_input == '-':
        num1 = float(input("enter 1st number: "))
        num2 = float(input("enter 2nd number: "))
        minus(num1, num2)
    elif user_input == '*':
        num1 = float(input("enter 1st number: "))
        num2 = float(input("enter 2nd number: "))
        multiply(num1, num2)
    elif user_input == '/':
        num1 = float(input("enter 1st number: "))
        num2 = float(input("enter 2nd number: "))
        divide(num1, num2)
    elif user_input == 'h':
        view_history()
    elif user_input == 'lr':
        user_input2 = input("OPERATION 2: ")
        num = float(input("enter number: "))
        lastResult(user_input2, num)
    else:
        print("Unknown input!")
