def frequency_analysis(text):
    # Инициализируем словарь для хранения частот
    frequencies = {}

    # Приводим текст к нижнему регистру
    text = text.lower()

    # Подсчитываем количество букв в тексте
    total_letters = sum(c.isalpha() for c in text)

    # Подсчитываем частоты букв
    for char in text:
        if char.isalpha():
            frequencies[char] = frequencies.get(char, 0) + 1

    # Выводим частоты букв в процентах
    for char, count in frequencies.items():
        percentage = (count / total_letters) * 100
        print(f"Буква '{char}' встречается в тексте {percentage:.2f}%")

# Пример использования
with open("C:/Users/Andrey/Desktop/27-166b.txt", "r", encoding="utf-8") as file:
    text = file.read()

frequency_analysis(text)
