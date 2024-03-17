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

#Задача 7
#Дана строка. Необходимо найти минимальное из имеющихся в ней натуральных чисел.
import re

def FindMinNumber(String):
    # Паттерн для поиска всех натуральных чисел в строке
    pattern = r'\b\d+\b'

    # Найти все натуральные числа в строке
    Numbers = re.findall(pattern, String)

    # Преобразовать числа из строкового формата в целочисленный и найти минимальное
    MinNumber = min(map(int, Numbers), default=None)

    return MinNumber

String = input("Введите строку: ")
MinNumber = FindMinNumber(String)
if MinNumber is not None:
    print("Минимальное натуральное число в строке:", MinNumber)
else:
    print("В строке нет натуральных чисел.")
