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


#Задача 6
#Отсортировать строки в порядке увеличения медианного значения выборки строк (прошлое медианное значение удаляется из выборки и производится поиск нового медианного значения).
def CalculateMedian(List):
    SortedList = sorted(List)
    n = len(SortedList)
    if n % 2 == 0:
        return (SortedList[n//2 - 1] + SortedList[n//2]) / 2
    else:
        return SortedList[n//2]

def SortByMedian(Strings):
    MedianValues = [CalculateMedian([ord(char) for char in String]) for String in Strings]
    SortedStrings = [String for i, String in sorted(zip(MedianValues, Strings))]
    return SortedStrings

NumOfStrings = int(input("Введите количество строк: "))
Strings = []

# Считываем строки с клавиатуры и добавляем их в список
for i in range(NumOfStrings):
    String = input("Введите строку: ")
    Strings.append(String)

# Сортируем строки по медианному значению ASCII-кода символов
SortedStrings = SortByMedian(Strings)

# Выводим упорядоченный список строк
print("Отсортированные строки по медианному значению выборки:")
for String in SortedStrings:
    print(String)

#Задача 8
#Отсортировать строки в порядке увеличения квадратичного отклонения между средним весом ASCII-кода символа в строке и максимально среднего ASCII-кода тройки подряд идущих символов в строке. 
from itertools import combinations

def CalculateMean(lst):
    # Функция для вычисления среднего значения списка чисел
    if len(lst) == 0:
        return 0
    return sum(lst) / len(lst)

def CalculateMaxMeanTriple(string):
    # Функция для вычисления максимального среднего значения ASCII-кода тройки символов в строке
    maxMean = 0
    # Перебираем все возможные тройки символов в строке
    for triple in combinations(string, 3):
        # Вычисляем среднее значение ASCII-кода для тройки символов
        tripleMean = sum(ord(char) for char in triple) / 3
        # Если это значение больше текущего максимального, обновляем его
        if tripleMean > maxMean:
            maxMean = tripleMean
    return maxMean

def CalculateQuadraticDeviation(meanAscii, maxMeanTriple):
    # Функция для вычисления квадратичного отклонения между двумя значениями
    return (meanAscii - maxMeanTriple) ** 2

def SortByQuadraticDeviation(strings):
    # Функция для сортировки строк по увеличению квадратичного отклонения между средним весом ASCII-кода символа и максимальным средним ASCII-кодом тройки подряд идущих символов
    sortedStrings = sorted(strings, key=lambda x: CalculateQuadraticDeviation(CalculateMean([ord(char) for char in x]), CalculateMaxMeanTriple(x)))
    return sortedStrings

numOfStrings = int(input("Введите количество строк: "))
stringsList = []

# Считываем строки с клавиатуры и добавляем их в список
for _ in range(numOfStrings):
    string = input("Введите строку: ")
    stringsList.append(string)

# Сортируем строки по увеличению квадратичного отклонения между средним весом ASCII-кода символа и максимальным средним ASCII-кодом тройки подряд идущих символов
sortedStrings = SortByQuadraticDeviation(stringsList)

# Выводим упорядоченный список строк
print("Отсортированные строки по увеличению квадратичного отклонения:")
for string in sortedStrings:
    print(string)

#Задача 11
#Отсортировать строки в порядке квадратичного отклонения дисперсии максимального среднего веса ASCII-кода тройки символов в строке от максимального среднего веса ASCII-кода тройки символов в первой строке.
from itertools import combinations

def MeanAsciiTriple(string):
    # Функция для вычисления среднего ASCII-кода тройки символов в строке
    return sum(ord(char) for char in string) / len(string)

def MaxMeanTriple(strings):
    # Функция для вычисления максимального среднего ASCII-кода тройки символов среди всех строк
    maxMean = 0
    for string in strings:
        tripleMean = MeanAsciiTriple(string)
        if tripleMean > maxMean:
            maxMean = tripleMean
    return maxMean

def VarianceMaxMeanTriple(string, maxMean):
    # Функция для вычисления дисперсии максимального среднего ASCII-кода тройки символов в строке
    tripleMeans = [sum(ord(char) for char in triple) / 3 for triple in combinations(string, 3)]
    variance = sum((mean - maxMean) ** 2 for mean in tripleMeans) / len(tripleMeans)
    return variance

def QuadraticDeviationVariance(strings, maxMeanFirst):
    # Функция для вычисления квадратичного отклонения дисперсии максимального среднего ASCII-кода тройки символов в строке
    quadraticDeviations = [VarianceMaxMeanTriple(string, maxMeanFirst) for string in strings]
    return quadraticDeviations

def SortByQuadraticDeviationVariance(strings, maxMeanFirst):
    # Функция для сортировки строк по увеличению квадратичного отклонения дисперсии
    quadraticDeviations = QuadraticDeviationVariance(strings, maxMeanFirst)
    sortedStrings = [string for _, string in sorted(zip(quadraticDeviations, strings))]
    return sortedStrings

# Считываем строки с клавиатуры и добавляем их в список
numOfStrings = int(input("Введите количество строк: "))
stringsList = [input("Введите строку: ") for _ in range(numOfStrings)]

# Вычисляем максимальное среднее значение ASCII-кода тройки символов в первой строке
maxMeanFirst = MeanAsciiTriple(stringsList[0])

# Сортируем строки по увеличению квадратичного отклонения дисперсии
sortedStrings = SortByQuadraticDeviationVariance(stringsList, maxMeanFirst)

# Выводим упорядоченный список строк
print("Отсортированные строки по увеличению квадратичного отклонения дисперсии:")
for string in sortedStrings:
    print(string)

