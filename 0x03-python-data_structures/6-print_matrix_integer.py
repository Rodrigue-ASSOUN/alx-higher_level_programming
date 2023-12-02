#!/usr/bin/python3
def print_matrix_integer(matrix):
    for row in matrix:
        row_string = ""
        for element in row:
            row_string += str(element) + " "
        print(row_string)
