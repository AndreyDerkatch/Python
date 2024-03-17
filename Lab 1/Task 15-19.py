#Вариант 5, Задачи 17, 29, 41, 53
def SwapMinMax(array):
    # Функция для замены местами минимального и максимального элементов массива
    if not array:
        return array

    minIndex = array.index(min(array))
    maxIndex = array.index(max(array))

    # Меняем местами минимальный и максимальный элементы массива
    array[minIndex], array[maxIndex] = array[maxIndex], array[minIndex]

    return array

def CheckMaxInRange(array, a, b):
    # Функция для проверки наличия максимального элемента массива в заданном интервале
    if not array:
        return False

    maxElement = max(array)
    return a <= maxElement <= b

def AverageAbs(array):
    # Функция для вычисления среднего арифметического модулей элементов массива
    if not array:
        return None

    return sum(abs(num) for num in array) / len(array)
