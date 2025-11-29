from linal import *
import random
from typing import Callable
#частное разностное отношение 
def partial_difference_quotient(f: Callable[[Vector], float], v: Vector, i: int, h: float) -> float:
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]  # Fixed: enumerate order
    return (f(w) - f(v)) / h



#вычисление градиента
def estimate_gradient(f: Callable[[Vector], float], v:Vector,h:float = 0.0001):
    return [partial_difference_quotient(f,v,i,h) for i in range(len(v))]


#Использование градиента

def gradient_step(v: Vector, gradient: Vector, step_size: float) -> Vector:  # Fixed return type
    # assert len(v) == len(gradient)
    step = scalar_multiply(step_size, gradient)
    return add(v, step)


def sum_of_squares_gradient(v:Vector)->Vector:
    return (2*v_i for v_i in v)

v = [random.uniform(-10, 10) for i in range(3)]

for epoch in range(1000):
    grad = sum_of_squares_gradient(v)
    v = gradient_step(v, grad, -0.01)

    print(epoch, v)

print(distance(v, [0,0,0]))
assert distance(v, [0,0,0]) < 0.001