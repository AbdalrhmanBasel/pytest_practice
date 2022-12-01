"""
Task 8
1. implement the Vector(x, y) class with operations
of addition, subtraction and multiplication by a number

To be edited:
1. Class is not used. # DONE
2. Usage of any libraries is forbidden. # DONE
"""


class Vector_Calculator:

    # Vector Addition
    def addition(self, x, y, r):
        for i in range(len(x)):
            # iterate through columns
            for j in range(len(x[0])):
                r[i][j] = x[i][j] + y[i][j]

        for i in r:
            print(i)

    # Vector Subtraction
    def subtraction(self, x, y, r):
        for i in range(len(x)):
            # iterate through columns
            for j in range(len(x[0])):
                r[i][j] = x[i][j] - y[i][j]

        for i in r:
            print(i)

    def multiplication(self, x, y, r):

        for i in range(len(x)):
            # iterate through columns of Y
            for j in range(len(y[0])):
                # iterate through rows of Y
                for k in range(len(y)):
                    r[i][j] += x[i][k] * y[k][j]

        for rs in r:
            print(rs)

    def division(self, x, y, r):

        for i in range(len(x)):
            # iterate through columns of Y
            for j in range(len(y[0])):
                # iterate through rows of Y
                for k in range(len(y)):
                    r[i][j] += x[i][k] / y[k][j]

        for rs in r:
            print(rs)


x = [[2, 2, 2]]
y = [[5, 8, 1, 2]]
r = [[0, 0, 0, 0]]

if __name__ == "__main__":
    calculator = Vector_Calculator()
    calculator.addition(x, y, r)
    calculator.subtraction(x, y, r)
    calculator.multiplication(x, y, r)
