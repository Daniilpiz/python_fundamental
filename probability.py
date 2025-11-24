import math

SQRT_TWO_PI = math.sqrt(2*math.pi)


def normal_pdf(x:float, mu:float = 0, sigma:float = 1) -> float:
    return (math.exp(-(x-mu)**2 / 2 /sigma**2) / (SQRT_TWO_PI*sigma))