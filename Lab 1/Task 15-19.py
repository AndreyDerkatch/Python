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
