"""
History calculator.
The calculator should work in the REPL format: we enter a value,
the result is calculated and displayed on the screen, the program again prompts you
to enter a value. After each operation, a list with a history of previously
performed operations should be displayed.
"""

import time

history = []


def timer():
    time.sleep(1)
    print("")
    print("--------------------------------------------------------------------------")


print("Enter '+' for addition:")
print("Enter '-' for subtraction:")
print("Enter '*' for multiplication:")
print("Enter '/' for division:")
print("Enter 'h' to check history:")
print("Enter 'quit' to end the calculator:")

while True:

    user_input = input("OPERATION: ")

    if user_input == 'quit':
        break

    elif user_input == '+':
        print("")
        num1 = float(input("enter first number: "))
        num2 = float(input("enter first number: "))
        sum = str(num1 + num2)
        print("")
        print("The sum is " + sum)

        history.append(f'{num1}' + ' + ' + f'{num2}' + ' = ' + f'{sum}')
        print(history)
        timer()

    elif user_input == '-':
        print("")
        num1 = float(input("enter first number: "))
        num2 = float(input("enter first number: "))
        diff = str(num1 - num2)
        print("")
        print("The difference is " + diff)

        history.append(f'{num1}' + ' - ' + f'{num2}' + ' = ' + f'{diff}')
        print(history)
        timer()

    elif user_input == '*':
        print("")
        num1 = float(input("enter first number: "))
        num2 = float(input("enter first number: "))
        product = str(num1 * num2)
        print("")
        print("The product is " + product)

        history.append(f'{num1}' + ' * ' + f'{num2}' + ' = ' + f'{product}')
        print(history)
        timer()

    elif user_input == '/':
        print("")
        num1 = float(input("enter first number: "))
        num2 = float(input("enter first number: "))
        div = str(num1 / num2)
        print("")
        print("The division is " + div)

        history.append(f'{num1}' + ' / ' + f'{num2}' + ' = ' + f'{div}')
        print(history)
        timer()

    elif user_input == 'h':
        print(history)

    else:
        print("Unknown input!")
