# Task: construct an interpolation polynomial in the Newtonian form of the 9th and 19th degrees for
# function y = sin(x) on an interval from 0 to pi
# Result: function graphs
import numpy as np
import matplotlib.pyplot as plt

a = 0
c = np.pi

# ---------------------------------------------------------------------------------------------------------------------

def func(x):
    return np.sin(x)

# ---------------------------------------------------------------------------------------------------------------------

def b(s, i, X, Y):
    if s == 0:
        A = Y[i]
    elif s == 1:
        A = (Y[i+1] - Y[i]) / (X[i+1] - X[i])
    else:
        A = (b(s - 1, i + 1, X, Y) - b(s - 1, i, X, Y)) / (X[s + i] - X[i])
    return A

# ---------------------------------------------------------------------------------------------------------------------

def Inter(n, x, X, B):
    I = 0
    for i in range(n):
        D = 1
        P = 1
        for j in range(i):
            P *= (x-X[j])
        D *= P*B[i]
        I += D
    return I

# ---------------------------------------------------------------------------------------------------------------------

def Ravn_Set(n):
    X = np.zeros(n+1)
    Y = np.zeros(n+1)
    for i in range(n+1):
        X[i] = (i * (c - a)) / n
        Y[i] = func(X[i])
    B = []
    for i in range(n+1):
        B.append(b(i, 0, X, Y))
    x = np.linspace(a, c, 600)
    y = Inter(n, x, X, B)
    return x,y

# ---------------------------------------------------------------------------------------------------------------------

plt.figure()
x1, y1 = Ravn_Set(9)
x2, y2 = Ravn_Set(19)
x0 = np.linspace(a, c, 600)
y0 = func(x0)
plt.plot(x0, y0, label='sin(x)')
plt.plot(x1, y1, label='Инт.многочл.Ньютона 9-го')
plt.plot(x2, y2, label='Инт.многочл.Ньютона 19-го')
plt.legend()
plt.show()