data = [[1, -1, -1, 1], [-1, 1, -1, 1], [-1, -1, 1, 1], [-1, 1, 1, 1], [1, -1, 1, 1], [1, 1, -1, 1], [1, 1, 1, 1]]
# AdaBoost - ансамбль алгоритмов через взвешенное голосование
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

print(adaBoost(data))