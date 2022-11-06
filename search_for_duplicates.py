import random
import time

# сортировка Хоара (быстрая сортировка)
def quicksort(a):
    if len(a) < 2:
        return a
    else:
        pivot = a[0]  # опорный элемент
        less = [i for i in a[1:] if i <= pivot]  # подмассив эл-в меньше опорного
        greater = [i for i in a[1:] if i > pivot]  # подмассив эл-в больше опорного
        return quicksort(less) + [pivot] + quicksort(greater)

# метод проходит по отсортированному массиву и ищет самую длинную последовательность равных эл-в
def sorting_search(a):
    a = quicksort(a)
    count = 1
    max_c = 1
    value = a[0]
    i = 1
    result = []

    while i < len(a):
        if value == a[i]:
            count += 1
        else:
            if max_c < count:
                result.clear()
                result.append(value)
                max_c = count
            else:
                if max_c == count:
                    result.append(value)
            value = a[i]
            count = 1
        i += 1

    if count > max_c:
        result.clear()
        result.append(value)
    else:
        if count == max_c:
            result.append(value)

    print(result)


# метод перебирает все эл-ты массива и считает количество каждого значения
def enumeration(a):
    max_k = 0
    result = []
    for i in range(len(a)):
        c = 0                       # обнуляем счетчик
        value = a[i]                # присваеваем новое значение
        for j in range(len(a)):
            if value == a[j]:
                c += 1              # если встретили элемент увеличиваем кол-во
        if c > max_k:
            result.clear()          # очищаем список с элементами которых максимальное количество
            result.append(value)
            max_k = c
        elif c == max_k:
            result.append(value)
    print(set(result))


# a = [int(i) for i in input().split()]     # ввод с клавиатуры
i = 0
avg_sortings = 0
avg_enumeration = 0
while i < 10:
    a = [random.randint(0, 100) for i in range(25000)]
    b = a.copy()
    start_sorting = time.monotonic()  # запуск таймера
    sorting_search(a)
    result_time_sort = time.monotonic() - start_sorting
    print(f'Подсчет сортировкой: {result_time_sort}')
    avg_sortings += result_time_sort

    start_enumiration = time.monotonic()  # запуск таймера
    enumeration(b)
    result_time_enum = time.monotonic() - start_enumiration
    print(f'Подсчет перебором: {result_time_enum}')
    avg_enumeration += result_time_enum
    i += 1

print(f'Среднее время сортировкой: {avg_sortings / 10}')
print(f'Среднее время перебором: {avg_enumeration / 10}')
