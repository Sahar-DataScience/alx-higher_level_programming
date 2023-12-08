#!/usr/bin/python3
import numpy

def square_matrix_simple(matrix):

    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            matrix[i][j] = matrix[i][j]**2
    return matrix
