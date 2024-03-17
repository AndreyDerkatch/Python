#Вариант 5
#Задача 7
#Дана строка, состоящая из символов латиницы. Образуют ли прописные символы этой строки палиндром?
def IsItPalindrome(string):
    # Создаем список из прописных букв строки
    letters = [letter for letter in string if letter.isalpha() and letter.isupper()]
    # Проверяем список на симметрию
    return letters == letters[::-1]

string = input("Введите строку из символов латиницы: ")
if IsItPalindrome(string):
    print("Прописные символы образуют палиндром.")
else:
    print("Прописные символы не образуют палиндром.")
