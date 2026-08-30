import numpy as np

# Coefficient matrix
A = np.array([[2, 3],
              [4, -5]])

# Constant matrix
B = np.array([12, -2])

# Solve the equations
X = np.linalg.solve(A, B)

print("Value of x =", X[0])
print("Value of y =", X[1])