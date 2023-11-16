import numpy as np
import random
class RandomMatrixGenerator:
    def __init__(self, Mlines, Ncolumns, Krank):
        self.lineSize   = Mlines
        self.columnSize = Ncolumns
        self.rank       = Krank

    def generateRandomMatrix(self):
        seed       = np.random.default_rng(8080)
        vectorU = seed.integers(-20,20,(self.columnSize,1))
        transposevectorV = seed.integers(-20,20,(1,self.lineSize))

        finalMatrix = vectorU @ transposevectorV

        for i in range(self.rank-1):
            vectorU = seed.integers(-20,20,(self.columnSize,1))
            transposevectorV = seed.integers(-20,20,(1,self.lineSize))

            auxiliarMatrix = vectorU @ transposevectorV
            finalMatrix = np.add(finalMatrix,auxiliarMatrix)

        return finalMatrix

