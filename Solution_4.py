import numpy as np
from scipy.linalg import lu

def LU_dec(A):
    rangA = A.shape[0]  # Ранг матрицы
    a = A.copy()
    L = np.eye(rangA)
    P = np.eye(rangA)
    for i in range(rangA - 1):
        P_i = np.eye(rangA)
        m = np.argmax(np.abs(a[i:, i]))  # Индекс максимального по модулю элемента в столбце i
        P_i[m + i], P_i[i] = P_i[i].copy(), P_i[m + i].copy()
        a = P_i @ a
        l = np.eye(rangA)
        g = a[i + 1:, i] / a[i, i]
        l[i + 1:, i] = -g
        a = l @ a
        l[i + 1:, i] = g
        L = L @ P_i @ l
        P = P @ P_i
    return [P, P.T @ L, a]

def printres(C):
    if np.all(C == B):
        print('_' * 20)
        print("Для матрицы B:")
        print('_'*20)
    elif np.all(C == A):
        print('_' * 20)
        print("Для матрицы A:")
        print('_' * 20)
    q = LU_dec(C)[0]
    w = LU_dec(C)[1]
    e = LU_dec(C)[2]
    [print("     P ручным способом  ", q, sep='\n', end='\n' * 2) if i == 0
     else print("     L ручным способом  ", w, sep='\n', end='\n' * 2) if i == 1
    else print("     U ручным способом ", e, sep='\n', end='\n' * 2) for i in range(3)]
    print("     A = P*L*U ручным способом ", q @ w @ e, sep='\n', end='\n'*2)
    scipy_lu(C)

def scipy_lu(C):
    r = lu(C)[0]
    t = lu(C)[1]
    y = lu(C)[2]
    [print("     P с помощью scipy  ", r, sep='\n', end='\n' * 2) if i == 0
     else print("     L с помощью scipy  ", t, sep='\n', end='\n' * 2) if i == 1
    else print("     U с помощью scipy ", y, sep='\n', end='\n' * 2) for i in range(3)]
    print("     A = P*L*U с помощью scipy ", r @ t @ y, sep='\n')


t = np.pi/4
A = np.array([[np.cos(t), -np.sin(t)],
              [np.sin(t), np.cos(t)]])
B = np.array([[ 0, -1, -2],
              [-4,  6,  3],
              [-4, -2,  8]])

printres(A)
printres(B)