import numpy as np

matrix = np.array([[4,1,1,7],
             [-2,6,1,9],
             [1,1,5,-6]], dtype=float)

def gauss_seidel(A, b, x0, max_iter, tol):
    n = len(A)
    x = x0[:]
    for itr in range(max_iter):
        x_old = x[:]
        for i in range(n):
            sigma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sigma) / A[i][i]
        if max(abs(x[i] - x_old[i]) for i in range(n)) < tol:
            return x
    return x

max_iter = 100
tol = 1e-6
A = matrix[:,:-1]
b = matrix[:,-1]
x0 = np.zeros(len(b))

solusi = gauss_seidel(A,b,x0,max_iter,tol)
print(solusi)

# Nama : Dwi Budi Fitri Adi
# Kelas : TIF RP 24D
# NPM : 24552011093