#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx in row:
            print("{:d}".format(idx), end="")
            if idx != row[-1]:
                print(" ", end="")
        print("")
