"""
Task 7 - list comprehensions
Through the command line, # DONE
1. List of integers is entered # DONE
2. Numbers separated by spaces. # DONE
3. Print a list of even numbers. # DONE
4. Print a list of odd numbers. # DONE
5. Numbers less than 0 Use manual enumeration,
6. If some element is not a number, output -1. # DONE
DO NOT use built-in functions.
"""

# from enum import Enum
#
# class Day(Enum):
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#
# print(Day.MONDAY)
# print(Day.MONDAY.name)
# print(Day.MONDAY.value)
#
# print(Day.TUESDAY.name)


list = []
num = 0
looping = True

while looping:
    try:
        list_input = int(input("Enter Numbers For List: "))
        if list_input == "=":
            looping = False
        else:
            list.append(list_input)
    except:
        list.append(-1)

    # printing list
    string_list = [str(x) for x in list]
    print(" ".join(string_list))

# using list comprehension
even_list = [x for x in list if x % 2 == 0]
odd_list = [x for x in list if x % 2 == 1]

print("Even numbers in the list: " + even_list)
print("Odd numbers in the list: " + odd_list)
