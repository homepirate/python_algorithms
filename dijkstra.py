import math


def get_link_v(v, D):
    for i, w in enumerate(D[v]):
        if w > 0: # если вес(есть путь) между вершинами
            yield i


def arg_min(T, S):
    amin = -1
    m = max(T)
    for i, t in enumerate(T):
        if t < m and i not in S:
            m = t
            amin = i

    return amin


D = ((0, 3, 1, 3, math.inf, math.inf), # матрица смежности графа
     (3, 0, 4, math.inf, math.inf, math.inf),
     (1, 4, 0, math.inf, 7, 5),
     (3, math.inf, math.inf, 0, math.inf, 2),
     (math.inf, math.inf, 7, math.inf, 0, 4),
     (math.inf, math.inf, 5, 2, 4, 0))


N = len(D)
T = [math.inf] * N

v = 0 # начальная вершина
S = {v} # храним вершины, которые уже просмотрели
T[v] = 0


while v != -1:
    for j in get_link_v(v, D):
        if j not in S:
            w = T[v] + D[v][j] # высчитываем текущий вес. T[v] начальный вес, D[v][j] вес дуги
            if w < T[j]: # сохраняем минимальное значение веса
                T[j] = w

    v = arg_min(T, S) # выбираем вершину с минимальным весом для следующий итерации
    if v > 0:
        S.add(v)


print(T)