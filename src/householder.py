import numpy as np
import numpy.linalg as linalg

class Householder:
    def __init__(self, matrixA):
        self.matrixA = matrixA
        self.lineNumber = len(matrixA)
        self.incompleteHouseholderMatrix = []
        self.completeHouseholderMatrix = []

    def getHouseholderMatrix(self):
        A1 = []
        for line in range(self.lineNumber):
            A1.append(self.matrixA[line, 0])

        arrayA1 = np.array(A1)
        normA1 = linalg.norm(arrayA1)

        base_vector = np.array([[1]] + [[0]] * (self.lineNumber - 1))

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
        householderMatrix = identity - 2 * matricesMultiplication

        self.incompleteHouseholderMatrix = householderMatrix

        return householderMatrix

    def completeHouseholderMatrix(self, size):
        householderMatrix = np.identity(size)

        incompleteMatrixSize = len(self.incompleteHouseholderMatrix)

        startPoint = size - incompleteMatrixSize
        householderMatrix[startPoint:, startPoint:] = self.incompleteHouseholderMatrix

        self.completehouseholdermatrix = np.array(householderMatrix)

        return householderMatrix
