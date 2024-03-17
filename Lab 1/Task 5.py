#Задание 5
#Дана строка. Необходимо найти все даты которые описаны в виде "31 февраля 2007"
import re
def FindDates(String):
    # Паттерн для поиска дат в формате "число месяца год"
    PatternDates = r'\b\d{1,2}\s(?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\s\d{4}\b'
    # Найти все даты в строке
    FoundDates = re.findall(PatternDates, String)
    return FoundDates

String = input("Введите строку: ")
Dates = FindDates(String)
print("Найденные даты:")
for Date in Dates:
    print(Date)
