#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        sq = list(map(lambda r: r**2, row))
        new_matrix.append(sq)
    return new_matrix
