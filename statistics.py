from typing import List
from collections import Counter
from linal import sum_of_squares, dot
import math
import matplotlib.pyplot as plt

num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


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


# xs = [8, 34, -15, 77, 55, 1200, 23, 91, 41, 62,
#  5, 88, 19, 104, 72, -450, 33, 67, 95, 11,
#  50, 82, 29, 115, 600, 44, 76, 3, 98, 25,
#  60, 87, 38, 2200, 71, 15, 52, 79, 100, 31,
#  66, 92, 47, 12, 83, -120, 58, 21, 74, 96,
#  40, 69, 17, 110, 800, 36, 61, 7, 89, 27,
#  53, 85, 45, 1500, 78, 14, 49, 70, 102, 35,
#  64, 90, 42, 9, 81, -300, 57, 24, 73, 94,
#  39, 68, 20, 106, 950, 46, 75, 2, 97, 26,
#  59, 84, 37, 1800, 65, 13, 51, 80, 99, 30]
# print(median(xs))

# print(mean(xs))
# print(standard_deviation(xs))
# print(interquartile_range(xs))
# 

daily_minutes = [1,68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,54.01,38.79,47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45,21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,26.97,36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,28.66,29.08,37.28,15.28,24.17,22.31,30.17,25.53,19.85,35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,24.26,31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,27.21,26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,36.65,18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,29.79,32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,35.35,28.48,9.08,24.62,20.12,35.26,19.92,31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,24.42,9.82,23.39,30.93,15.03,21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]

daily_hours = [dm / 60 for dm in daily_minutes]

def covariance(xs: List[float], ys: List[float]) -> float:
    assert len(xs) == len(ys), "xs and ys must have same number of elements"

    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)

assert 22.42 < covariance(num_friends, daily_minutes) < 22.43
assert 22.42 / 60 < covariance(num_friends, daily_hours) < 22.43 / 60

def correlation(xs: List[float], ys: List[float]) -> float:
    """Measures how much xs and ys vary in tandem about their means"""
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x / stdev_y
    else:
        return 0    # if no variation, correlation is zero

assert 0.24 < correlation(num_friends, daily_minutes) < 0.25
assert 0.24 < correlation(num_friends, daily_hours) < 0.25

plt.scatter(num_friends, daily_minutes, color = "red", marker='d')
plt.xlabel("число друзей")
plt.ylabel("число минутб проводимых на сайте еждневно")


outlier = num_friends.index(100)    # index of outlier

num_friends_good = [x
                    for i, x in enumerate(num_friends)
                    if i != outlier]

daily_minutes_good = [x
                      for i, x in enumerate(daily_minutes)
                      if i != outlier]

daily_hours_good = [dm / 60 for dm in daily_minutes_good]

assert 0.57 < correlation(num_friends_good, daily_minutes_good) < 0.58
assert 0.57 < correlation(num_friends_good, daily_hours_good) < 0.58

plt.scatter(num_friends_good, daily_minutes_good)
# plt.xlabel("число друзей")
# plt.ylabel("число минутб проводимых на сайте еждневно")
plt.show()
