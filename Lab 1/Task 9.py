#Прочитать список строк с клавиатуры. Упорядочить по длине строки.
def SortByLength(Strings):
    # Упорядочить строки по их длине
    SortedStrings = sorted(Strings, key=len)
    return SortedStrings

NumberOfStrings = int(input("Введите количество строк: "))
Strings = []

# Считать строки с клавиатуры и добавить их в список
for _ in range(NumberOfStrings):
    String = input("Введите строку: ")
    Strings.append(String)

# Упорядочить строки по длине
SortedStrings = SortByLength(Strings)

# Вывести упорядоченные строки
print("Упорядоченные строки по длине:")
for String in SortedStrings:
    print(String)
