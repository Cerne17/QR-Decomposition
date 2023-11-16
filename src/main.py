from backsubstitution import *
import random
import numpy as np
from matricesgeneration import RandomMatrixGenerator

def main():
    rows = int(input("Insert the number of columns: "))
    columns = int(input("Insert the number of rows: "))

    rank = int(input("Insert the rank: "))
    while (rank > min(rows, columns)):
        print("The rank must be less than the minimum between the number of rows and columns.")
        rank = int(input("Insert the rank: "))
    matrix = RandomMatrixGenerator(rows, columns, rank).generateRandomMatrix()
    print("Generated matrix: ")
    print(matrix)

    vector = []

    for i in range(columns):
        vector.append([random.randint(1, 10)])

    vector = np.array(vector)
    vector.transpose()

    print("Generated vector: ")
    print(vector)

    print("Solution: ")
    print(backSubstitution(matrix, vector))

if __name__ == "__main__":
    main()
