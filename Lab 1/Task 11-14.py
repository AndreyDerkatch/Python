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
