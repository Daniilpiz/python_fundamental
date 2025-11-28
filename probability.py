import math
import matplotlib.pyplot as plt
import random

#кумулятивная функция распределения
def uniform_cdf(x:float) -> float:
    if x<0: return 0
    elif x<1: return x
    else: return 1


data = sorted([random.uniform(-1, 2) for i in range(10000)])
plt.plot(data, [uniform_cdf(x) for x in data])
plt.show()

#нормальное распределение
SQRT_TWO_PI = math.sqrt(2*math.pi)

def normal_pdf(x:float, mu:float = 0, sigma:float = 1) -> float:
    return (math.exp(-(x-mu)**2 / 2 /sigma**2) / (SQRT_TWO_PI*sigma))

xs = [x/10.0 for x in range(-100, 100)]
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs],'-', label = 'мю = 0, сигма = 1', color = "green")
plt.plot(xs, [normal_pdf(x, sigma = 2) for x in xs],'.', label = 'мю = 0, cигма = 2',color = 'red')
plt.plot(xs, [normal_pdf(x, sigma = 0.5) for x in xs],'--', label = 'мю = 0, cигма = 0.5',color = 'blue')
plt.plot(xs, [normal_pdf(x, sigma = 1, mu= -1) for x in xs],':', label = 'мю = -1, cигма = 1',color = 'black')

plt.legend()
plt.title("Различные функции плотности вероятности")
plt.show()


# нормальные кумулятивные функции
def normal_cdf(x:float,mu: float, sigma:float = 1 ) -> float:
    return (1 + math.erf((x-mu) / math.sqrt(2) / sigma)) / 2

plt.plot(xs, [normal_cdf(x, sigma=1, mu= 0) for x in xs],'-', label = 'мю = 0, сигма = 1', color = "green")
plt.plot(xs, [normal_cdf(x, sigma = 2, mu= 0) for x in xs],'.', label = 'мю = 0, cигма = 2',color = 'red')
plt.plot(xs, [normal_cdf(x, sigma = 0.5, mu = 0) for x in xs],'--', label = 'мю = 0, cигма = 0.5',color = 'blue')
plt.plot(xs, [normal_cdf(x, sigma = 1, mu= -1) for x in xs],':', label = 'мю = -1, cигма = 1',color = 'black')

plt.legend(loc = 4)
plt.title("Различные нормальные кумулятивные функции")
plt.show()


#инвертирование кумулятивной функции
#используем бинарный поиск для нахождения приближенного значения

def inverse_normal_cdf(p:float, mu:float = 0, sigma:float = 1, tolerance: float = 0.00001)-> float:
    if mu != 0 or sigma != 1:
        return mu+sigma+inverse_normal_cdf(p, tolerance=tolerance)
    
    low_z = -10.0
    hi_z = 10.0

    while hi_z-low_z>tolerance:
        mid_z = (low_z+hi_z) / 2 #рассмотреть среднюю точку
        mid_p = normal_cdf(mid_z, mu=0, sigma=1) # и рассмотреть значение cdf от этой точки

        if mid_p<p:
            low_z = mid_z #средняя точка низкая искать выше

        else: hi_z = mid_z #средняя точка высокая искать ниже
    return mid_z


plt.plot(xs, [inverse_normal_cdf(x, sigma=1, mu= 0) for x in xs],'-', label = 'мю = 0, сигма = 1', color = "green")
plt.plot(xs, [inverse_normal_cdf(x, sigma = 2, mu= 0) for x in xs],'.', label = 'мю = 0, cигма = 2',color = 'red')
plt.plot(xs, [inverse_normal_cdf(x, sigma = 0.5, mu = 0) for x in xs],'--', label = 'мю = 0, cигма = 0.5',color = 'blue')
plt.plot(xs, [inverse_normal_cdf(x, sigma = 1, mu= -1) for x in xs],':', label = 'мю = -1, cигма = 1',color = 'black')

plt.legend(loc = 4)
plt.title("Различные инвертированные нормальные кумулятивные функции")
plt.show()