# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 1, 2, 5
# Вывод: 1, 3, 5, 7, 9

def printArithmeticProgression(first_element, difference, total_elements):
    progression = [(first_element + i * difference) for i in range(total_elements)]
    print(*progression)

first_element = int(input("Введите 1-ый член арифметической прогрессии: "))
difference = int(input("Введите разность арифметической прогрессии: "))
total_elements = int(input("Введите общее количество арифметической прогрессии: "))

printArithmeticProgression(first_element, difference, total_elements)