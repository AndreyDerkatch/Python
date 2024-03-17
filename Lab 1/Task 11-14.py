#Задача 2
#Отсортировать строки в порядке увеличения среднего веса ASCII-кода символа строки
def AverageAsciiWeight(string):
    # Функция для вычисления среднего веса ASCII-кода символов строки
    if len(string) == 0:
        return 0
    asciiSum = sum(ord(char) for char in string)
    return asciiSum / len(string)

numOfStrings = int(input("Введите количество строк: "))
stringsList = []

# Считываем строки с клавиатуры и добавляем их в список
for _ in range(numOfStrings):
    string = input("Введите строку: ")
    stringsList.append(string)

# Упорядочиваем список строк по среднему весу ASCII-кода символов
sortedList = sorted(stringsList, key=AverageAsciiWeight)

# Выводим упорядоченный список строк
print("Строки, упорядоченные по среднему весу ASCII:")
for string in sortedList:
    print(string)
