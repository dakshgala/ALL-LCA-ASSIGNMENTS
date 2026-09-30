# Assignment 4: Create arrays (matrices) and add two matrices


def read_matrix(name, rows, cols):
    """Read a matrix row by row from the user."""
    print(f"\nEnter elements of matrix {name}:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1} ({cols} values, space-separated): ").split()))
        if len(row) != cols:
            raise ValueError(f"Expected {cols} values in each row.")
        matrix.append(row)
    return matrix


def add_matrices(A, B, rows, cols):
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] + B[i][j]
    return result


def print_matrix(name, M):
    print(f"\n{name}:")
    for row in M:
        print(" ".join(f"{val:5}" for val in row))


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

A = read_matrix("A", rows, cols)
B = read_matrix("B", rows, cols)

C = add_matrices(A, B, rows, cols)

print_matrix("Matrix A", A)
print_matrix("Matrix B", B)
print_matrix("A + B", C)

# Optional: the same thing using NumPy arrays (pip install numpy)
# import numpy as np
# print(np.array(A) + np.array(B))
