# Градиентный спуск для фнкции с многими переменными
import sympy as sym

def grad_2(c): # Градиент для функции с двумя переменными
    w1, w0 = sym.symbols('w1 w0') # Создание рабочих символов
    sigm = lambda x: 1 / (1 + sym.E**(-x))
    f = sym.ln(sigm(w1 + w0)) + sym.ln(1 - sigm(-w1 + w0)) + sym.ln(1 - sigm(-2*w1 + w0))
    d_f_w1, d_f_w0 = f.diff(w1), f.diff(w0) # Получение формулы частной производной по X и по Y
    f1, f2 = sym.lambdify([w1, w0], d_f_w1), sym.lambdify([w1, w0], d_f_w0) # Расчет производной по X и по Y
    xx = [f1(c[0], c[1]), f2(c[0], c[1])]
    print(f"Gradient = {round(f1(c[0], c[1]), 2)}, {round(f2(c[0], c[1]), 2)}")
    return xx # Возвращаем градиент
h = 0.1
A=[0, 0]
for _ in range(1):
    g = grad_2(A)
    A = [round(A[i] - h * g[i], 3) for i in range(2)]
    print(f"w1 = {A[0]}, w0 = {A[1]}")

def grad_2_2(c): # Градиент для функции с двумя переменными
    u, d = -0.2, 0.05
    w1, w0 = sym.symbols('w1 w0') # Создание рабочих символов
    sigm = lambda x: 1 / (1 + sym.E**(-x))
    f = sym.ln(sigm((w1*(-1) + w0) * u + d)) + sym.ln(sigm((w1*(-2) + w0) * u + d))
    d_f_w1, d_f_w0 = f.diff(w1), f.diff(w0) # Получение формулы частной производной по X и по Y
    f1, f2 = sym.lambdify([w1, w0], d_f_w1), sym.lambdify([w1, w0], d_f_w0) # Расчет производной по X и по Y
    xx = [f1(c[0], c[1]), f2(c[0], c[1])]
    print(f"Gradient = {round(f1(c[0], c[1]), 2)}, {round(f2(c[0], c[1]), 2)}")
    return xx # Возвращаем градиент
h = 0.1
A=[1, 0]
for _ in range(1):
    g = grad_2_2(A)
    A = [round(A[i] - h * g[i], 3) for i in range(2)]
    print(f"Для генератора: w1 = {A[0]}, w0 = {A[1]}")


