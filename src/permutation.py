import numpy as np

def newPermutationMatrix(order, column1, column2):
    matrixP = np.identity(order)

    if column1 != column2:
        matrixP[column1][column1] = 0
        matrixP[column2][column2] = 0
        matrixP[column1][column2] = 1
        matrixP[column2][column1] = 1

    return matrixP
