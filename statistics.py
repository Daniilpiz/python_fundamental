from typing import List


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

