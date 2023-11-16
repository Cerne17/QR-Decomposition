import numpy as np
from qrdecomposition import qrDecompositionNonPermutation, qrDecompositionComplete
from matricesgeneration import RandomMatrixGenerator

def minimumSquaresDecomposition(matrixA, debug=False, analysis=False):
    transposedMatrixA = matrixA.transpose()
    matrixV, matrixR, matrixP = qrDecompositionComplete(transposedMatrixA)

    transposedMatrixR = matrixR.transpose()
    transposedMatrixV = matrixV.transpose()

    rowMatrixU, matrixT = qrDecompositionNonPermutation(transposedMatrixR)
    matrixU = matrixP @ rowMatrixU

    if debug:
        print("---------- Minimum Squares Decomposition ----------")
        print("Final Matrix A: ")
        print(matrixA)
        print()
        print("Default Matrix U: ")
        print(matrixU)
        print()
        print("Final Matrix T: ")
        print(matrixT)
        print()
        print("Final Matrix V Transposed: ")
        print(transposedMatrixV)
        print()

    if analysis:
        print("---------- Minimum Squares Decomposition ----------")
        print("Matrix A: ")
        print(matrixA)
        print()
        print("Matrix U: ")
        print(matrixU)
        print()
        print("Matrix T: ")
        print(matrixT)
        print()
        print("Matrix V Transposed: ")
        print(transposedMatrixV)
        print()


    return matrixU, matrixT, transposedMatrixV

if __name__ == "__main__":

    matrixE = np.array([
        [ 230,   99,   -1],
        [ -91, -153, -178],
        [  -3, -147, -165]
        ])

    minimumSquaresDecomposition(matrixE, analysis=True)
