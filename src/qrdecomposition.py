import numpy as np
from householder import getHouseholderMatrix, completeHouseholderMatrix
import permutation as perm
from matricesgeneration import RandomMatrixGenerator

def qrDecompositionNonPermutation(matrixA, debug=False, analysis = False):
    matrixQ      = getHouseholderMatrix(matrixA).transpose()
    matrixR      = getHouseholderMatrix(matrixA) @ matrixA
    lineNumbersA = len(matrixA)

    minimumDimension = min(len(matrixA), len(matrixA[0]))
    
    if debug:
        print("---------- QR Non Permutation ----------")
        print("Default Matrix A: ")
        print(matrixA)
        print()
        print("Default Matrix Q: ")
        print(matrixQ)
        print()
        print("Default Matrix R: ")
        print(matrixR)
        print()

    for i in range(1, minimumDimension):
        auxiliarMatrix = np.array(matrixR[i:, i:])
        incompleteHouseholderMatrix = getHouseholderMatrix(auxiliarMatrix)

        householderMatrix = completeHouseholderMatrix(incompleteHouseholderMatrix,lineNumbersA)

        matrixR = householderMatrix @ matrixR
        matrixQ = matrixQ @ householderMatrix.transpose()

    if debug:
        print("---------------------")
        print("Final Matrix A: ")
        print(matrixA)
        print()
        print("Final Matrix Q: ")
        print(matrixQ)
        print()
        print("Final Matrix R: ")
        print(matrixR)
        print()
        print("---------- QR Non Permutation End ----------")

    if analysis:
        print("---------- QR Non Permutation ----------")
        print("Matrix A: ")
        print(matrixA)
        print()
        print("Matrix Q: ")
        print(matrixQ)
        print()
        print("Matrix R: ")
        print(matrixR)
        print()
        print("Matrix QR: ")
        print(matrixQ @ matrixR)
        print()

    return matrixQ, matrixR

def qrDecompositionComplete(matrixA, debug=False, analysis = False):
    matrixR = matrixA
    matrixQ = np.identity(len(matrixA))
    matrixP = np.identity(len(matrixA[0]))

    if debug:
        print("---------- QR Complete ----------")
        print("Default Matrix A: ")
        print(matrixA)
        print()
        print("Default Matrix Q: ")
        print(matrixQ)
        print()
        print("Default Matrix R: ")
        print(matrixR)
        print()

    for i in range(0, min(len(matrixA), len(matrixA[0]))):

        norms = []
        auxiliarMatrix = np.array(matrixR[i:, i:])
        
        for j in range(len(auxiliarMatrix)):
            norms.append(np.linalg.norm(auxiliarMatrix[:,j]))

        tradingPositions = norms.index(max(norms)) + i

        currentP = perm.newPermutationMatrix(len(matrixA[0]), i, tradingPositions)

        matrixP = matrixP @ currentP
        matrixR = matrixR @ currentP

        auxiliarMatrix = np.array(matrixR[i:, i:])

        incompleteHouseholderMatrix = getHouseholderMatrix(auxiliarMatrix)
        householderMatrix = completeHouseholderMatrix(incompleteHouseholderMatrix, len(matrixA))

        matrixR = householderMatrix @ matrixR
        matrixQ = matrixQ @ householderMatrix.transpose()
    
    if debug:
        print("---------------------")
        print("Final Matrix A: ")
        print(matrixA)
        print()
        print("Final Matrix Q: ")
        print(matrixQ)
        print()
        print("Final Matrix R: ")
        print(matrixR)
        print()
        print("Final Matrix P: ")
        print(matrixP)
        print()
        print("---------- QR Complete End ----------")

    if analysis:
        print("---------- QR Complete ----------")
        print("Matrix A: ")
        print(matrixA)
        print()
        print("Matrix Q: ")
        print(matrixQ)
        print()
        print("Matrix R: ")
        print(matrixR)
        print()
        print("Matrix QR: ")
        print(matrixQ @ matrixR)
        print()
        print("Matrix AP: ")
        print(matrixA @ matrixP)
        print()

    return matrixQ, matrixR, matrixP

if __name__ == "__main__":

    matrix = RandomMatrixGenerator(3,3,3).generateRandomMatrix()

    qrSolutionNonPermE = qrDecompositionNonPermutation(matrix, analysis=True)

    qrSolutionPermE = qrDecompositionComplete(matrix, analysis=True)
