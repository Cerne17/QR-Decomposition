import numpy as np
from householder import getHouseholderMatrix, completeHouseholderMatrix
import permutation as perm
from matricesgeneration import RandomMatrixGenerator

def qrDecompositionNonPermutation(matrixA, debug=False):
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

    return matrixQ, matrixR

def qrDecompositionComplete(matrixA, debug=False):
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

    return matrixQ, matrixR, matrixP

if __name__ == "__main__":
    # print("---------- QR Non Permutation ----------")

    # matrices33Complete = RandomMatrixGenerator(3, 3, 3)
    # matrixA = matrices33Complete.generateRandomMatrix()
    #
    # print("Matrix A:")
    # print(matrixA)
    # print()
    #
    # qrSolutionA = qrDecompositionNonPermutation(matrixA)
    #
    # print("Matrix Q:")
    # print(qrSolutionA[0])
    # print()
    # print("Matrix R:")
    # print(qrSolutionA[1])
    # print()
    #
    # matrices34 = RandomMatrixGenerator(4, 4, 4)
    # matrixB = matrices34.generateRandomMatrix()
    #
    # print("Matrix B:")
    # print(matrixB)
    # print()
    #
    # qrSolutionB = qrDecompositionNonPermutation(matrixB)
    #
    # print("Matrix Q:")
    # print(qrSolutionB[0])
    # print()
    # print("Matrix R:")
    # print(qrSolutionB[1]) 
    #
    # print("---------- QR Complete ----------")
    #
    # matrixC = matrices33Complete.generateRandomMatrix()
    #
    # print("Matrix C:")
    # print(matrixC)
    # print()
    #
    # qrSolutionC = qrDecompositionComplete(matrixC)
    #
    # print("Matrix Q:")
    # print(qrSolutionC[0])
    # print()
    # print("Matrix R:")
    # print(qrSolutionC[1])
    # print()
    # print("Matrix P:")
    # print(qrSolutionC[2])
    # print()
    #
    # matrixD = matrices34.generateRandomMatrix()
    #
    # print("Matrix D:")
    # print(matrixD)
    # print()
    #
    # qrSolutionD = qrDecompositionComplete(matrixD)
    #
    # print("Matrix Q:")
    # print(qrSolutionD[0])
    # print()
    # print("Matrix R:")
    # print(qrSolutionD[1])
    # print()
    # print("Matrix P:")
    # print(qrSolutionD[2])
    # print()

    matrixE = np.array([
        [-27, -30, 33, -12],
        [4, 17, -52, 34],
        [40, 51, 16, 6],
        [7, 13, 11, 4]
        ])

    qrSolutionNonPermE = qrDecompositionNonPermutation(matrixE, debug=True)

    qrSolutionPermE = qrDecompositionComplete(matrixE, debug=True)
