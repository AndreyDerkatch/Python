import re

def validate_zip_code(zip_code):
    # Проверяем, соответствует ли строка формату почтового индекса (5 цифр)
    if re.match(r'^\d{5}$', zip_code):
        return True
    else:
        return False

def get_zip_code(zip_code):
    # Проверяем, соответствует ли строка формату почтового индекса (5 цифр)
    if re.match(r'^\d{5}$', zip_code):
        return zip_code
    else:
        raise ValueError("Некорректный аргумент: не является почтовым индексом")

# Пример использования
user_input = input("Введите почтовый индекс: ")

try:
    print(get_zip_code(user_input))
except ValueError as e:
    print(e)
