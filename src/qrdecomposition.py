import numpy as np
from householder import getHouseholderMatrix, completeHouseholderMatrix
from matricesgeneration import RandomMatrixGenerator

def qrDecompositionNonPermutation(matrixA):
    matrixQ      = getHouseholderMatrix(matrixA).transpose()
    matrixR      = getHouseholderMatrix(matrixA) @ matrixA
    lineNumbersA = len(matrixA)

    minimumDimension = min(len(matrixA), len(matrixA[0]))

    for i in range(1, minimumDimension):
        auxiliarMatrix = np.array(matrixR[i:, i:])
        incompleteHouseholderMatrix = getHouseholderMatrix(auxiliarMatrix)

        householderMatrix = completeHouseholderMatrix(incompleteHouseholderMatrix,lineNumbersA)

        matrixR = householderMatrix @ matrixR
        matrixQ = matrixQ @ householderMatrix.transpose()

    return matrixQ, matrixR

matrices33Complete = RandomMatrixGenerator(3, 3, 3)
matrices55Complete = RandomMatrixGenerator(5, 5, 5)
matrixA = matrices33Complete.generateRandomMatrix()

print("Matrix A:")
print(matrixA)
print()

qrSolutionA = qrDecompositionNonPermutation(matrixA)

print("Matrix Q:")
print(qrSolutionA[0])
print()
print("Matrix R:")
print(qrSolutionA[1])

matrices34 = RandomMatrixGenerator(4, 4, 4)
matrixB = matrices34.generateRandomMatrix()

print("Matrix A:")
print(matrixB)
print()

qrSolutionB = qrDecompositionNonPermutation(matrixB)

print("Matrix Q:")
print(qrSolutionB[0])
print()
print("Matrix R:")
print(qrSolutionB[1])
