#Вариант 5
def Main():
    # Считываем количество кубиков у Ани и Бори
    n, m = map(int, input().split())

    # Создаем множества для цветов кубиков Ани и Бори
    AniaColors = set()
    BoryaColors = set()

    # Считываем номера цветов кубиков Ани
    for _ in range(n):
        color = int(input())
        AniaColors.add(color)

    # Считываем номера цветов кубиков Бори
    for _ in range(m):
        color = int(input())
        BoryaColors.add(color)

    # Находим пересечение множеств цветов кубиков
    BothColors = AniaColors.intersection(BoryaColors)
    OnlyAniaColors = AniaColors.difference(BoryaColors)
    OnlyBoryaColors = BoryaColors.difference(AniaColors)

    # Выводим результаты
    print(len(BothColors))
    print(*sorted(BothColors))

    print(len(OnlyAniaColors))
    print(*sorted(OnlyAniaColors))

    print(len(OnlyBoryaColors))
    print(*sorted(OnlyBoryaColors))

Main()
