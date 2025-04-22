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
A = [[4, -1, 1],
    [-2, 6, 1],
    [1, 1, 5]]
b = [7, 9, -6]
x0 = [0,0,0]
tol = 1e-6
solusi = gauss_seidel(A,b,x0,max_iter,tol)
print(f"x0 = {solusi[0]:.5f}, x1 = {solusi[1]:.5f}, x2 = {solusi[2]:.5f}")
# Nama : Dwi Budi Fitri Adi
# Kelas : TIF RP 24D
# NPM : 24552011093
