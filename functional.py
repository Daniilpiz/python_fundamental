# функция zip

from typing import List, Optional, Dict, Iterable, Tuple


list1 = ['a', 'b', 'c']
list2 = [1,2,3]

pairs = [pair for pair in zip(list1, list2)]

print(pairs)

#распаковка аргументов

letters, numbers = zip(*pairs)
print(letters)
print(numbers)


#args и kwargs

def magic(*args, **kwargs):
    print(f"Безымянные аргументы: {args}")
    print(f"аргументы по ключу: {kwargs}")

magic(1, 2, key = "word", key2 = "word2")



def other_way_magic(x, y, z):
    return x+y+z

x_y_list = [1, 2]
z_dict = {"z":3}

assert other_way_magic(*x_y_list, **z_dict) == 6, "1+2+3 должно БЫТЬ РАВНО 6"


#аннотации типов

def total(xs:List[int]) -> float:
    return sum(xs)

values:List[int] = []
best_so_far: Optional[float] = None


counts:Dict[str, int] = {"a":1, "b":2}

evens: Iterable[int] = (x for x in range(10) if x%2==0)


triple: Tuple[int, float, int] = (10, 2.5, 3)