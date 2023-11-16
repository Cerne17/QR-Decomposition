import numpy as np
from qrdecomposition import *
from minimumsquares import *

def backSubstitution(matrixA, vectorB):
    rowsSizeA = len(matrixA)
    columnsSizeA = len(matrixA[0])
    rankA = np.linalg.matrix_rank(matrixA)

    vectorX = np.zeros((columnsSizeA, 1))

    if (rowsSizeA == columnsSizeA and columnsSizeA == rankA):
        matrixQ, matrixR = qrDecompositionNonPermutation(matrixA)
        vectorX = np.linalg.inv(matrixR) @ matrixQ.transpose() @ vectorB
        print("Case A")

    if (rowsSizeA > columnsSizeA and columnsSizeA == rankA):
        matrixQ, matrixR = qrDecompositionNonPermutation(matrixA)

        matrixR1 = matrixR[:rankA, :]
        matrixQ1 = matrixQ[:, :rankA]

        vectorX = (np.linalg.inv(matrixR1) @ matrixQ1.transpose() @ vectorB)
        print("Case C")

    if (rowsSizeA < columnsSizeA and rowsSizeA == rankA):
        matrixQ, matrixR = qrDecompositionNonPermutation(matrixA.transpose())
        vectorY = vectorX

        transposedMatrixR = matrixR.transpose()
        transposedMatrixR1 = transposedMatrixR[:, :rowsSizeA]

        vectorY[:rowsSizeA] = np.linalg.inv(transposedMatrixR1) @ vectorB

        vectorX = matrixQ @ vectorY
        print("Case D")

    if (rankA < min(rowsSizeA, columnsSizeA)):
        matrixU, matrixT, transposedMatrixV = minimumSquaresDecomposition(matrixA)
        vectorY = vectorX

        matrixU1 = matrixU[:, :rankA]
        matrixT1 = matrixT[:rankA, :rankA]

        vectorY[:rankA] = np.linalg.inv(matrixT1) @ matrixU1.transpose() @ vectorB
        vectorX = transposedMatrixV.transpose() @ vectorY
        print("Case B")

    return vectorX
