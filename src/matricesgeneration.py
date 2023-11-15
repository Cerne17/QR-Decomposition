import numpy as np
import random
class RandomMatrixGenerator:
    def __init__(self, Mlines, Ncolumns, Krank):
        self.lineSize   = Mlines
        self.columnSize = Ncolumns
        self.rank       = Krank

    def generateRandomMatrix(self):
        matrix  = []

        for i in range(self.columnSize):
            matrix.append([])

            for j in range(self.lineSize):
                matrix[i].append(0)

        for i in range(self.rank):
            vectorU = []
            vectorV = []

            # Generating u
            for j in range(self.lineSize):
                vectorU.append([random.randint(0, 10)])
            
            # Generating v
            for k in range(self.columnSize):
                vectorV.append([random.randint(0, 10)])

            matrix += np.dot(np.array(vectorU), np.array(vectorV).transpose())

        return matrix

