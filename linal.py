from typing import List

Vector = List[float]

height_weight_age = [175,
                     68,
                     40]

grades = [95,
          80,
          75,
          62]

#cложение двух векторов
def add(v: Vector, w: Vector):
    assert len(v)==len(w), "Векторы должны иметь равную длину"

    return [v_i+w_i for v_i, w_i in zip(v, w)]

assert add([1, 2,3], [4,5,6]) == [5, 7, 9], "Это ЧЗХ?!"

#вычитание
def substract(v: Vector, w: Vector):
    assert len(v)==len(w), "Векторы должны иметь равную длину"

    return [v_i-w_i for v_i, w_i in zip(v, w)]

#cумма N векторов
def vectors_sum(vectors: List[Vector]) -> Vector:
    assert vectors, "Где векторы/а"

    num_elements = len(vectors[0])
    
    assert all(len(v) == num_elements for v in vectors), "Разные размеры"

    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

print(vectors_sum([[1,2], [3, 4], [5, 6], [7, 8]]))


assert vectors_sum([[1,2], [3, 4], [5, 6], [7, 8]]) == [16, 20] , "Ошибочка"


#cкалярное произведение

def scalar_multiply(c: float, v:Vector) -> Vector:
    return [c*v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2,4,6], 'Ну это невозможно'


#поэлементное среднее арифметическое
def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)
    return scalar_multiply(1/n, vectors_sum(vectors))

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4], "Не не не"

#скалярное произведение двух векиторов
def dot(v:Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "Длины векторов должны быть равны"

    return sum(v_i*w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32, "Такого быть не может"


#cумма квадратов
def sum_of_squares(v:Vector)->float:
    return dot(v, v)

assert sum_of_squares([1,2,3])==14

import math

def magnitude(v:Vector)->float:
    return math.sqrt(sum_of_squares(v))

assert magnitude([3,4]) == 5

#квадрат расстояния между векторами
def squared_distance(v:Vector, w:Vector) -> Vector:
    return sum_of_squares(substract(v, w))


#расстояние между векторами
def distance(v:Vector, w:Vector)->float:
    return magnitude(substract(v, w))