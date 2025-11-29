from linal import Vector, add, distance, scalar_multiply, vector_mean
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

v = [random.uniform(-10, 10) for i in range(4)]

for epoch in range(10000):
    grad = sum_of_squares_gradient(v)
    v = gradient_step(v, grad, -0.01)

    print(epoch, v)

print(distance(v, [1,1,2,3]))
assert distance(v, [0,0,0, 0]) < 0.001




#применение градиентного спуска
inputs = [(x, x*20 +5 ) for x in range(-50, 50)]
def linear_gradient(x:float, y:float, theta:Vector)->Vector:
    slope, intercept = theta
    predicted = slope*x + intercept

    error = predicted - y

    squarred_error = error**2
    grad = [2*error*x, 2*error]
    return grad


theta = [random.uniform(-1, 1), random.uniform(-1, 1)]

learning_rate = 0.001

for epoch in range(500_000):
    grad = vector_mean([linear_gradient(x,y, theta) for x,y in inputs])
    theta = gradient_step(theta, grad, -learning_rate)
    print(epoch, theta)

slope, intercept = theta
assert 19.9 < slope < 20.1 #наклон должен быть примерно 20
assert 4.9 < intercept < 5.1 #пересечение должно быть равным примерно 5