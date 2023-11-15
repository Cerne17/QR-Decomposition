import numpy as np
from qrdecomposition import qrDecompositionNonPermutation, qrDecompositionComplete
from matricesgeneration import RandomMatrixGenerator

def minimumSquaresDecomposition(matrixA):
    transposedMatrixA = matrixA.transpose()
    matrixV, matrixR, matrixP = qrDecompositionComplete(transposedMatrixA)

    transposedMatrixR = matrixR.transpose()
    transposedMatrixV = matrixV.transpose()

    rowMatrixU, matrixT = qrDecompositionNonPermutation(transposedMatrixR)
    matrixU = matrixP @ rowMatrixU

    return matrixU, matrixT, transposedMatrixV

matrices33Complete = RandomMatrixGenerator(3, 3, 3)

matrixA = matrices33Complete.generateRandomMatrix()

print("Matrix A:")
print(matrixA)
print()

minimumSquaresSolution = minimumSquaresDecomposition(matrixA)

print("Matrix U:")
print(minimumSquaresSolution[0])
print()

print("Matrix T:")
print(minimumSquaresSolution[1])
print()

print("Matrix V:")
print(minimumSquaresSolution[2])
print()
