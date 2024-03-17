#Вариант 5

#Задача 5
#Дана строка. Необходимо найти наибольшее количество идущих подряд символов кириллицы.
import re

def FindLongestSubsring(String):
    # Паттерн для поиска подстрок кириллицы
    pattern = r'[а-яА-Я]+'
    # Найти все подстроки кириллицы в строке
    substring = re.findall(pattern, String)
    # Найти подстроку с максимальной длиной
    LongestSubsrting = max(substring, key=len, default="")

    return LongestSubsrting

String = input("Введите строку: ")
LongestSubsrting = FindLongestSubsring(String)
print("Наибольшее количество идущих подряд символов кириллицы:", LongestSubsrting)
