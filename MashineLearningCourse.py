def evkld(list_1, lst): # Евклидово расстояние
    s = 0
    for i in range(len(lst)):
        try:
            s += ((list_1[i] - lst[i]) ** 2)
        except:
            continue
    return round(s ** 0.5, 2)

def mnhttn(list_1, lst): # Метрика Манхеттен
    s = 0
    for i in range(len(lst)):
        try:
            s += abs(list_1[i] - lst[i])
        except:
            continue
    return s
    
def max_mrtk(list_1, lst): # MAX метрика
    mx = 0
    for i in range(len(lst)):
        try:
            mx = max(abs(list_1[i] - lst[i]), mx)
        except:
            continue
    return mx
    
def normalise(lst): # Нормализация прзнака
    max_i, min_i = max(lst), min(lst)
    return [((x - min_i)/(max_i - min_i)) for x in lst]

def Sp(lst): # Среднее квадратическое отклонение
    mdll = sum(lst)/len(lst)
    return (sum((x - mdll)**2 for x in lst)/(len(lst) - 1))**0.5

def middle_normalise(lst): # Нормализация прзнака через среднее квадратическое отклонение
    mdll = sum(lst)/len(lst)
    sp = Sp(lst)
    return [round((x - mdll)/sp, 2) for x in lst] # !!! Округление

# Коэфф. корреляции
def get_correlation_c(P,Q):
    mdll_P, mdll_Q = sum(P)/len(P), sum(Q)/len(Q)
    return round((sum([i * j for i, j in zip(P, Q)]) - len(P) * mdll_P * mdll_Q) / ((len(P) - 1) * Sp(P) * Sp(Q)), 2)

# Восстановление данных с помощью метрик
def data_recovery(func, *args):
    k = args[0].index(None)
    known_val = [i for i in args[0] if i != None]
    data = [[x for i, x in enumerate(j) if i != k] for j in args[1:]]
    d = []
    for i, x in enumerate(known_val): # Получили список [(known_val, func()), (known_val, func())...]
        d.append(tuple([x, func(args[0], data[i])]))
    return round(sum([i[0] / i[1] for i in d])/sum([1 / i[1] for i in d]), 2)

def MAE_MAPE(list_1, list_2): # Качество модели линейной регрессии
    MAE = sum([abs(x - y) for x, y in zip(list_1, list_2)])/len(list_1)
    if 0 in list_1:
        zero_indx = [i for i, x in enumerate(list_1) if x == 0]
        list_1 = [x for i, x in enumerate(list_1) if i not in zero_indx]
        list_2 = [x for i, x in enumerate(list_2) if i not in zero_indx]
    MAPE = (sum([abs((x - y)/x) for x, y in zip(list_1, list_2)])/len(list_1)) * 100
    return f"MAE = {MAE}, MAPE = {MAPE}"

from sklearn import linear_model as lm
# Create linear regression object
def linear_reg():
    lr = lm.LinearRegression()
    lr.fit([[0],[1],[2],[3]], [0,1,0,3])
    return f"Intercept: {lr.intercept_}, Coefficient: , {lr.coef_}"

def gini(data): # Неопределённость Gini для вложенного списка, где последний подсписок - целевой признак
    answer = {}
    # Костыль: Условная вероятность того, что i-тый элемент в D2 = Y при условии что что i-тый элемент в D1 = P
    def kostil(D1, D2, Y, P):
        counter = 0
        if P in D1:
            for i in range(len(D1)):
                if D1[i] == P and D2[i] == Y:
                    counter += 1
            return counter / D1.count(P)
        return 0

    for i in range(len(data) - 1):
        P1 = data[i].count(0)/len(data[i]) * kostil(data[i], data[-1], 0, 0) * kostil(data[i], data[-1], 1, 0)
        P2 = data[i].count(1)/len(data[i]) * kostil(data[i], data[-1], 0, 1) * kostil(data[i], data[-1], 1, 1)
        answer[i] = round(P1 + P2, 2)
    return answer # Словарь, где ключ - номер признака(подсписка) в исходном вложенном списке

# AdaBoost - ансамбль алгоритмов через взвешенное голосование.
# data - вложенный список, где последний элеммент подсписка - целевой признак
# а остальные - предсказанные целевые признаки по разным алгоритмам
import math
def adaBoost(data):
    u = 1 / len(data) # начальные веса
    U = [u for _ in range(len(data))] # список весов
    for i in range(2):
        Bad = [] # Ошибки классификаторов
        for i in range(len(data[0]) - 1):
            uuu = 0
            for j, x in enumerate(U):
                if data[j][i] != data[j][-1]:
                    uuu += x
            Bad.append(uuu)
        classifier = min(Bad)
        classifier_index = Bad.index(classifier)

        weight = 0.5 * math.log((1 - classifier) / classifier)
        for i, u in enumerate(U):
            U[i] = u * math.exp(-weight * data[i][classifier_index] * data[i][-1])
        for i, u in enumerate(U):
            U[i] = round(u / sum(U), 3)
    
    answer = [(round(sum([b * x[i] for i, b in enumerate(Bad)]), 3), x[-1]) for x in data]
    return answer 

# Численное дифференцирование для градиентного спуска
def numeric_diff(func, delta, point):
    return (func(point-2*delta) - 8*func(point-delta) + 8*func(point+delta) - func(point+2*delta))/12*delta

import sympy as sym
def grad_2(c): # Градиент для функции с двумя переменными
    x, y = sym.symbols('x y') # Создание рабочих символов
    f = x**2 + 10 * y**2 # Наша исходная функция
    d_f_x, d_f_y = f.diff(x), f.diff(y) # Получение формулы частной производной по X и по Y
    f1, f2 = sym.lambdify(x, d_f_x), sym.lambdify(y, d_f_y) # Расчет производной по X и по Y
    c = [f1(c[0]), f2(c[1])]
    return c # Возвращаем градиент

# Градиентный спуск для фнкции с многими переменными
import sympy as sym

def grad_for_many(h=0.1, A=[10, 1]):
    for k in range(2):
        i, j = grad_2(A)
        A[0] = round(A[0] - h * i, 3)
        A[1] = round(A[1] - h * j, 3)
        print(k, A)

# Градиентный спуск для фнкции с одной переменной (модификация с шагом h)
import sympy as sym
import math

def grad_for_many(h=1, A=1):
    def grad(c):
        x = sym.symbols('x') # Создание рабочих символоы
        f = x**2 # Наша исходная функция
        d_f_x = f.diff(x) # Частная производная по X
        f1 = sym.lambdify(x, d_f_x) # Расчет производной по X
        c = f1(c)
        return c # Возвращаем градиент
    T = 1
    for n in range(1, 4):
        A = round(A - h * grad(A), 3)
        print(n, h, A)
        h = 1 * math.e ** (-n/T)

# Градиентный спуск для фнкции с многими переменными (модификация Adagrad)
import sympy as sym

def adagrad(h=0.1, A=[10, 1]):
    G = [0, 0] # Квадрат градиента (точнее сумма квадратов на данной итерации)
    E = 0.000000000000000001 # Очень малое число, чтобы не делить на 0
    answer = []
    for _ in range(5):
        i, j = grad_2(A)
        G = [G[0] + i**2, G[1] + j**2]
        A[0] = round(A[0] - h * i / (G[0] + E)**0.5, 3) # Первая координата новой точки
        A[1] = round(A[1] - h * j / (G[1] + E)**0.5, 3) # Вторая координата новой точки
        answer.append(A[:])
    return answer

# Градиентный спуск для функции с многими переменными (модификация Adam)
import sympy as sym

def adam(h=0.1, A=[10, 1]):
    B1 = B2 = 0.9 # Коэффициенты B1 и B2 показывают насколько быстро "забываются" даные
    m = r = [0, 0] # m и r накапливают информацию о взвешенном среднем градиента
    E = 0.000000000000000001 # Очень малое число, чтобы не делить на 0
    answer = []
    for k in range(1, 5):
        i, j = grad_2(A)
        G = [i**2, j**2] # Квадрат градиента
        m = [B1 * m[i] + (1 - B1) * G[i] for i in range(2)]
        r = [B2 * r[i] + (1 - B2) * G[i]**2 for i in range(2)]
        M = [m[i]/(1 - B1**k) for i in range(2)]
        R = [r[i]/(1 - B2**k) for i in range(2)]
        A = [round(A[i] - ((h * M[i]) / ((R[i] + E)**0.5)), 3) for i in range(2)] # Новые координаты точки
        answer.append(A[:])
    return answer

print(adam())

# Градиентный спуск для функции с многими переменными
import sympy as sym

def grad_2(c): # Градиент для функции с двумя переменными
    w1, w0 = sym.symbols('w1 w0') # Создание рабочих символов
    f = (-w1 + w0 - 1)**2 + (w0 - 0)**2
    d_f_w1, d_f_w0 = f.diff(w1), f.diff(w0) # Получение формулы частной производной по X и по Y
    f1, f2 = sym.lambdify([w1, w0], d_f_w1), sym.lambdify([w0, w1], d_f_w0) # Расчет производной по X и по Y
    xx = [f1(c[0], c[1]), f2(c[0], c[1])]
    print([f1(c[0], c[1]), f2(c[0], c[1])])
    return xx # Возвращаем градиент

def grad_for_many(h=0.1, A=[0, 0]):
    for _ in range(1):
        g = grad_2(A)
        A = [A[i] - h * g[i] for i in range(2)]
        print(f"w1 = {A[:][0]}, w0 = {A[:][1]}")