#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            a = 0
            for a in range(len(row)):
                if a < len(row) - 1:
                    print("{:d} ".format(row[a]), end="")
                else:
                    print("{:d}".format(row[a]))
