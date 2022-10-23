# Task 5 - *args, **kwargs
# Write a function that takes an iterable or an arbitrary number
# of arguments and finds their maximum. Do not use built-in functions.
# ENTER:
# find_max(5, 3, 8, 10, 3)
# OUTPUT: 10


def my_max(*args):
    result = 0

    for max in args:
        if max > result:
            result = max
    return result


print(my_max(5, 3, 8, 10, 3))


