
'''
# Градиентный спуск для фнкции с многими переменными
import sympy as sym

def grad_2(c): # Градиент для функции с двумя переменными
    w1, w2, w3, w4 = sym.symbols('w1 w2 w3 w4') # Создание рабочих символов
    kostil_1 = -sym.log(sym.E**(-w1 + w3)/(sym.E**(-w1 + w3)+sym.E**(-w2 + w4)))
    kostil_2 = -sym.log(sym.E**(w2 + w4)/(sym.E**(w2 + w4)+sym.E**(w1 + w3)))
    f = kostil_1 + kostil_2
    d_f_w1 = f.diff(w1)
    d_f_w2 = f.diff(w2)
    d_f_w3 = f.diff(w3)
    d_f_w4 = f.diff(w4)

    f1 = sym.lambdify([w1, w2, w3, w4], d_f_w1)
    f2 = sym.lambdify([w1, w2, w3, w4], d_f_w2)
    f3 = sym.lambdify([w1, w2, w3, w4], d_f_w3)
    f4 = sym.lambdify([w1, w2, w3, w4], d_f_w4)
    
    xx = [f1(c[0], c[1], c[2], c[3]), f2(c[0], c[1], c[2], c[3]), f3(c[0], c[1], c[2], c[3]), f4(c[0], c[1], c[2], c[3])]
#    print(f"Gradient = {round(f1(c[0], c[1]), 2)}, {round(f2(c[0], c[1]), 2)}")
    return xx # Возвращаем градиент
h = 0.1
A=[0, 0, 0, 0]
for _ in range(10):
    g = grad_2(A)
    A = [round(A[i] - h * g[i], 3) for i in range(4)]
    print(f"w1 = {A[0]}, w2 = {A[1]}, w3 = {A[2]}, w4 = {A[3]}")

'''
# Градиентный спуск для фнкции с многими переменными

'''
import sympy as sym

def grad_2(c): # Градиент для функции с двумя переменными
    w1, w2, w3, w4 = sym.symbols('w1 w2 w3 w4') # Создание рабочих символов
    f = ((-2*w1 + w2)*w3 + w4 - 4)**2 + ((2*w1 + w2)*w3 + w4 - 4)**2
    d_f_w1 = f.diff(w1)
    d_f_w2 = f.diff(w2)
    d_f_w3 = f.diff(w3)
    d_f_w4 = f.diff(w4)

    f1 = sym.lambdify([w1, w2, w3, w4], d_f_w1)
    f2 = sym.lambdify([w1, w2, w3, w4], d_f_w2)
    f3 = sym.lambdify([w1, w2, w3, w4], d_f_w3)
    f4 = sym.lambdify([w1, w2, w3, w4], d_f_w4)
    
    xx = [f1(c[0], c[1], c[2], c[3]), f2(c[0], c[1], c[2], c[3]), f3(c[0], c[1], c[2], c[3]), f4(c[0], c[1], c[2], c[3])]
#    print(f"Gradient = {round(f1(c[0], c[1], c[2], c[3]), 2)}, {round(f2(c[0], c[1], c[2], c[3]), 2)}, {round(f3(c[0], c[1], c[2], c[3]), 2)}, {round(f4(c[0], c[1], c[2], c[3]), 2)}")
    return xx # Возвращаем градиент
h = 0.1
A=[1, 1, 1, -1]
for _ in range(10):
    g = grad_2(A)
    A = [round(A[i] - 0.05 * g[i], 3) if i in (0, 1) else round(A[i] - 0.1 * g[i], 3) for i in range(4)]
    print(f"w1 = {A[0]}, w2 = {A[1]}, w3 = {A[2]}, w4 = {A[3]}")

'''
import sympy as sym

def grad_2(c): # Градиент для функции с двумя переменными
    w1, w2, w3 = sym.symbols('w1 w2 w3') # Создание рабочих символов
    f = (w1 + w3 - 1)**2 + (w3 - 0)**2 + (w1 + w2 + w3 - 1)**2 + (w1 - 1)**2 + (w2 - 0)**2
    d_f_w1 = f.diff(w1)
    d_f_w2 = f.diff(w2)
    d_f_w3 = f.diff(w3)

    f1 = sym.lambdify([w1, w2, w3], d_f_w1)
    f2 = sym.lambdify([w1, w2, w3], d_f_w2)
    f3 = sym.lambdify([w1, w2, w3], d_f_w3)
    
    xx = [f1(c[0], c[1], c[2]), f2(c[0], c[1], c[2]), f3(c[0], c[1], c[2])]
#    print(f"Gradient = {round(f1(c[0], c[1], c[2], c[3]), 2)}, {round(f2(c[0], c[1], c[2], c[3]), 2)}, {round(f3(c[0], c[1], c[2], c[3]), 2)}, {round(f4(c[0], c[1], c[2], c[3]), 2)}")
    return xx # Возвращаем градиент
h = 0.1
A=[0.02, 0.9, 0.9]
for _ in range(15):
    g = grad_2(A)
    A = [round(A[i] - 0.1 * g[i], 3) for i in range(3)]
    print(f"w1 = {A[0]}, w2 = {A[1]}, w3 = {A[2]}")

def duty(x1, x2, x3):
    return A[0]*x1 + A[1]*x2 + A[2]*x3

base = [[1, 0, 0], [0, 1, 1], [0, 0, 0], [1, 0, 1], [1, 1, 0], [0, 1, 1]]

for i in base:
    answer = duty(*i)
    print(1 if answer >= 0.8 else 0)