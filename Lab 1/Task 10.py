#Дан список строк с клавиатуры. Упорядочить по количеству слов в строке.

def WordCount(String):
    # Функция для подсчета количества слов в строке
    return len(String.split())

NumberOfStrings = int(input("Введите количество строк: "))
Strings = []

# Считываем строки с клавиатуры и добавляем их в список
for i in range(NumberOfStrings):
    String = input("Введите строку: ")
    Strings.append(String)

# Упорядочиваем список строк по количеству слов
SortedStrings = sorted(Strings, key=WordCount)

# Выводим упорядоченный список строк
print("Упорядоченные строки по количеству слов:")
for String in SortedStrings:
    print(String)
