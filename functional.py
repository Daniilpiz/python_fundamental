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


#визуализация данных

from matplotlib import pyplot as plt

#линейная диаграмма
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color = "green", marker = 'o', linestyle = 'solid')
plt.title("Номинальный ВВП")

plt.ylabel("Млрд долларов")
plt.show()

#столбчатая диаграмма 

movies = ["Филм1", "Фильм2", "Фильм3", "Фильм4", "Фильм5"]
num_oscras = [5, 11, 3, 8, 10]

plt.bar(range(len(movies)), num_oscras)
plt.title("Крутые фильмы")

plt.ylabel("Количество наград")
plt.xticks(range(len(movies)), movies)
plt.show()

#гистограмма

from collections import Counter
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

#Cгруппировать все оценки подецильно, но разместить 100 вместе с отметками по 90 и выше

histogram = Counter(min(grade// 10*10, 90) for grade in grades)

plt.bar([x+5 for x in histogram.keys()], histogram.values(), 10, edgecolor = (0, 0, 0))
'''
сдвинуть столбец влево на 5
каждому столбцу ширина 10
чёрные края для каждого столбца
'''

plt.axis([-5, 105, 0, 5]) #метки по Ох от -5 до 15, по Оу от 0 до 5

plt.xticks([10*i for i in range(11)]) #Метки по оси x от 0, 10 ... 100
plt.xlabel("Дециль")
plt.ylabel("Число студентов")

plt.title("Распределение оценок за экзамен")
plt.show()

#линейные графики

variance = [2**i for i in range(9)]
bias_squared = variance.copy()[::-1]
total_error = [x+y for x, y in zip(variance, bias_squared)]

xs = [i for i, _ in enumerate(variance)]

plt.plot(xs, variance, 'g-', label = 'дисперсия')
plt.plot(xs, bias_squared, 'r-', label = 'смещение^2')
plt.plot(xs, total_error, 'b:', label = 'cуммарная ошибка')

plt.legend(loc = 9)

plt.xlabel('Сложность модели')
plt.title("компромис между смещением и дисперсией")

plt.show()

#диаграммы рассеяния

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy = (friend_count, minute_count),
                 xytext= (5, -5),
                 textcoords='offset points')


plt.title("число минут против числа друзей")
plt.xlabel("число друзей")
plt.ylabel("число минутб проводимых на сайте еждневно")

plt.show()