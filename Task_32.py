# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:
# 3 4 2 5 7
# [4,6]
# Вывод:
# 1, 3

def createArray(total_elements):
    array = [int(input(f"Введите {i+1} элемент массива: ")) for i in range(total_elements)]
    return array

def findIndicesForElementsInRange(array, bottom_limit, top_limit):
    result_array = []
    for i in range(len(array)):
        if array[i] >= bottom_limit and array[i] <= top_limit:
            result_array.append(i)
    print(*result_array)

elements = int(input("Введите кол-во элементов массива: "))
top_limit = int(input("Введите верхнюю границу для проверки: "))
bottom_limit = int(input("Введите нижнюю границу для проверки: "))

result_array = createArray(elements)
print(*result_array)
findIndicesForElementsInRange(result_array, bottom_limit, top_limit)
