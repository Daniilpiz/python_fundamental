# функция zip

from typing import List


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


