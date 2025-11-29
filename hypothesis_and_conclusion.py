from typing import Tuple
import math
from probability import inverse_normal_cdf, normal_cdf  

#проверка статистической гипотезы

#аппроксимация биномиальной случайной величины нормальным распределением
def normal_approximation_to_binomial(n:int, p:float) -> Tuple[float, float]:
    mu = n*p
    q = 1-p
    sigma = math.sqrt(n*p*q)

    return mu, sigma


#вероятность, что переменная ниже порога
normal_probability_below = normal_cdf

#она лежит выше порога, если она не ниже порога
def normal_probability_above(lo:float, mu:float = 0, sigma:float = 1)->float:
    return 1-normal_cdf(lo, mu, sigma)


#она лежит междуусли меньше чем hi и больше чем lo
def normal_probability_between(lo:float, hi:float, mu:float = 0, sigma:float = 1)->float:
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)


#она лежит за пределами если не лежит между
def normal_probability_outside(lo:float, hi:float, mu:float = 0, sigma:float = 1)->float:
    return 1 - normal_probability_between(lo, hi, mu, sigma)


#верхняя граница
def normal_upper_bound(probability:float, mu:float = 0, sigma:float = 1)-> float:
    return inverse_normal_cdf(probability, mu, sigma)


#нижняя граница
def normal_lower_bound(probability:float, mu:float = 0, sigma:float = 1)-> float:
    return inverse_normal_cdf(1 - probability, mu, sigma)



def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """returns the symmetric (about the mean) bounds
    that contain the specified probability"""
    tail_probability = (1 - probability) / 2

    # upper bound should have tail_probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    # lower bound should have tail_probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound


mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

#проверка на ошибку 1-го порядка
lower_bound, upper_bound = normal_two_sided_bounds(0.95, mu_0, sigma_0)
print(lower_bound, upper_bound)

lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)
print(lo, hi)
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.5)


#проверка на ошибку второго порядка
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)

hi = normal_upper_bound(0.95, mu_1, sigma_1)
print(hi)

power = 1 - type_2_probability
print(power)


#надо продолжить по той же главе p-значения, доверительные интервалы, взлом p-значения, байесов вывод, проведение A/B тестирования