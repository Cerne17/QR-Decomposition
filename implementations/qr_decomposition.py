import numpy as np

def qr_decomposition_householder(A):
    rows, cols = A.shape
    Q = np.eye(A)
    R = np.copy(A)

    for col in range(cols):
        column = R[col:, col]
        sign = np.sign(column[0])
        norm = np.linalg.norm(column, ord=2)
        unit_vector = sign * norm * np.eye(1, len(column), 0) + column
        unit_vector /= np.linalg.norm(unit_vector, ord=2)

        R[col:, col:] -= 2 * np.outer(unit_vector, unit_vector.T) @ R[col:, col:]
        Q[col:, :] -= 2 * np.outer(unit_vector, np.dot(unit_vector, Q[col:, :]))

    return Q.T, R


matrix_A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

orthogonal_Q, upper_triangular_R = qr_decomposition_householder(matrix_A)

print("Matrix Q:")
print(orthogonal_Q)
print("\nMatrix R:")
print(upper_triangular_R)

# Verify the decomposition
reconstructed_A = np.dot(orthogonal_Q, upper_triangular_R)
print("\nReconstructed A (Q * R):")
print(reconstructed_A)
