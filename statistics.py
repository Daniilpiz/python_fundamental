from typing import List
from collections import Counter

from linal import sum_of_squares
import math

# cреднее арифметическое
def mean(xs: List[int]) -> float:
    return sum(xs)/len(xs)

#медиана

def median_odd(xs:List[float]) -> float:
    return sorted(xs)[len(xs)//2]

def median_even(xs:List[float]) -> float:
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs)//2

    return (sorted_xs[hi_midpoint-1]+sorted_xs[hi_midpoint])/2

def median(v:List[float]) -> float:
    return median_even(v) if len(v)%2==0 else median_odd(v)


#квантиль

def quantile(xs:List[float], p:float)->float:
    p_index = int(p*len(xs))

    return sorted(xs)[p_index]

#мода
def mode(xs:List[float])->float:
    counts = Counter(xs)
    max_count = max(counts.values())

    return [x_i for x_i, count in counts.items() if count == max_count]

# дисперсия
def de_mean(xs:List[float])->List[float]:
    x_bar = mean(xs)
    return [x-x_bar for x in xs]


def variance(xs: List[float])->float:
    assert len(xs)>=2, "дисперсия требует 2-х и больше элементов"

    n = len(xs)
    deviations = de_mean(xs)

    return sum_of_squares(deviations)/(n-1)


def standard_deviation(xs:List[float]) -> float:
    return math.sqrt(variance(xs))

#интерквартильный размах(не подвержен выбросам, в отличии от стандартного отклонения и размаха)
def interquartile_range(xs:List[float]) -> float:
    return quantile(xs,0.75)-quantile(xs, 0.25)
