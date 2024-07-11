import numpy as np

# problem 1
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# sum of a and b
sum_vector = a + b
print(f"Sum of vectors a and b: {sum_vector}")

# difference between a and b
diff_vector = a - b
print(f"Difference of vectors a and b: {diff_vector}")


# problem 2
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# sum of a and b
sum_matrix = A + B
print(f"Sum of matrices A and B: {sum_matrix}")

# difference between a and b
diff_matrix = A - B
print(f"Difference of matrices A and B: {diff_matrix}")


# problem 3
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])

# product of A and B
product_matrix = np.dot(A, B)
print(f"Product of matrices A and B: {product_matrix}")


# problem 4
a = np.array([1, 1, 2])

# magnitude of a
magnitude = np.linalg.norm(a)
print(f"Magnitude of vector a: {magnitude}")


# problem 5
A = np.array([[1, 2], [3, 4]])

# transpose A
transpose_matrix = A.T
print(f"Transpose of matrix A: {transpose_matrix}")
