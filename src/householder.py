import numpy as np
import numpy.linalg as linalg

def getHouseholderMatrix(matrixA):
    A1 = []
    lineNumber = len(matrixA)

    for line in range(lineNumber):
        A1.append([matrixA[line, 0]])

    arrayA1 = np.array(A1)
    # normA1 = linalg.norm(arrayA1)
    normA1 = linalg.norm(A1)

    base_vector = np.array([[1]] + [[0]] * (len(arrayA1) - 1))

    if arrayA1[0] < 0:
        vectorV = arrayA1 - normA1 * base_vector
    else:
        vectorV = arrayA1 + normA1 * base_vector

    if np.linalg.norm(vectorV) == 0:
        vectorU = vectorV
    else:
        vectorU = vectorV / np.linalg.norm(vectorV)

    matricesMultiplication = vectorU @ vectorU.transpose()
    identity = np.identity(len(matricesMultiplication))
    incompleteHouseholderMatrix = identity - 2 * matricesMultiplication

    return incompleteHouseholderMatrix  

def completeHouseholderMatrix(incompleteMatrix, size):
    householderMatrix = np.identity(size)

    incompleteMatrixSize = len(incompleteMatrix)

    startPoint = size - incompleteMatrixSize
    householderMatrix[startPoint:, startPoint:] = incompleteMatrix

    return householderMatrix
