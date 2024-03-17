#Вариант 5

#Задача 5
#Дана строка. Перемешать все символы строки в случайном порядке
import random

print("Введите слово: ")
word = input()
letters = list(word)
random.shuffle(letters)
shuffled_word = ''.join(letters)

print(shuffled_word)

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

#Задача 14
# Дана строка в которой записаны слова через пробел. Необходимо упорядочить слова по количеству букв в каждом слове.
def SortByLength(String):
    # Разделить строку на слова
    Words = String.split()
    # Отсортировать слова по длине с помощью функции sorted и ключа длины слова
    SortedWords = sorted(Words, key=len)
    # Вернуть объединенную отсортированную строку
    return ' '.join(SortedWords)

String = input("Введите строку с словами через пробел: ")
SortedString = SortByLength(String)
print("Упорядоченные слова по длине:", SortedString)
