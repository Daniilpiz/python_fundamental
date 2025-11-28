import math
import matplotlib.pyplot as plt
import random


def uniform_cdf(x:float) -> float:
    if x<0: return 0
    elif x<1: return x
    else: return 1


data = sorted([random.uniform(-1, 2) for i in range(10000)])
plt.plot(data, [uniform_cdf(x) for x in data])
plt.show()


SQRT_TWO_PI = math.sqrt(2*math.pi)

def normal_pdf(x:float, mu:float = 0, sigma:float = 1) -> float:
    return (math.exp(-(x-mu)**2 / 2 /sigma**2) / (SQRT_TWO_PI*sigma))

xs = [x/10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs],'-', label = 'мю = 0, сигма = 1', color = "green")
plt.plot(xs, [normal_pdf(x, sigma = 2) for x in xs],'.', label = 'мю = 0, cигма = 2',color = 'red')
plt.plot(xs, [normal_pdf(x, sigma = 0.5) for x in xs],'--', label = 'мю = 0, cигма = 0.5',color = 'blue')
plt.plot(xs, [normal_pdf(x, sigma = 1, mu= -1) for x in xs],':', label = 'мю = -1, cигма = 1',color = 'black')


plt.legend()
plt.title("Различные функции плотности вероятности")
plt.show()