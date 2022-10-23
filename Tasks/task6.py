# Task 6 - write a decorator that prints the
# input and output of a function to the console.

# TO FIX: input & output doesn't print by decorator
# Statue: FIXED

"""
TODO:
    1. Write Decorator.
    2. Decorator Prints Input Of The Function.
    3. Decorator Prints the Output Of the Function.
    # DONE
"""


def print_input_And_Output(func):
    def wrapper(*args, **kwargs):
        print("Inputs Of Function:", *args, **kwargs)
        func(*args, **kwargs)
        print("Output Of Function:", func(*args, **kwargs))
        return func(*args, **kwargs)

    return wrapper


@print_input_And_Output
def add(*args):
    return sum(args)


add(5, 2, 3, 1, 3, 4, 3)


