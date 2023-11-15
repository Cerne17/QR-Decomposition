import numpy as np
from householder import Householder
from matricesgeneration import RandomMatrixGenerator

class QRDecomposition:
    def __init__(self, matrixA):
        self.matrixA      = matrixA
        self.matrixQ      = Householder(matrixA).getHouseholderMatrix().transpose()
        self.matrixR      = Householder(matrixA).getHouseholderMatrix() @ matrixA
        self.lineNumbersA = len(matrixA)

    def qrDecompositionNonPermutation(self):
        minimumDimension = min(len(self.matrixA), len(self.matrixA[0]))

        for i in range(1, minimumDimension):
            auxiliarMatrix = np.array(self.matrixR[i:, i:])
            householder = Householder(auxiliarMatrix)
            incompleteHouseholderMatrix = householder.getHouseholderMatrix()
            householder.incompleteHouseholderMatrix = incompleteHouseholderMatrix

            completeHouseholderMatrix = householder.completeHouseholderMatrix(self.lineNumbersA)

            self.matrixR = completeHouseholderMatrix @ self.matrixR
            self.matrixQ = self.matrixQ @ completeHouseholderMatrix.transpose()

        return self.matrixQ, self.matrixR


matrices33Complete = RandomMatrixGenerator(3, 3, 3)
matrices55Complete = RandomMatrixGenerator(5, 5, 5)
matrixA = matrices33Complete.generateRandomMatrix()
matrixB = matrices55Complete.generateRandomMatrix()

print("Matrix A:")
print(matrixA)
print()

print("Matrix B:")
print(matrixB)
print()

qrSolutionA = QRDecomposition(matrixA).qrDecompositionNonPermutation()

print("Matrix Q:")
print(qrSolutionA[0])
print()
print("Matrix R:")
print(qrSolutionA[1])
