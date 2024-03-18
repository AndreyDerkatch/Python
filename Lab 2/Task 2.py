#Вариант 5
def RestoreAccess(files, queries):
    # Создаем словарь для хранения прав доступа к файлам
    fileAccess = {}
    for file, access in files:
        fileAccess[file] = set(access.split())

    # Обрабатываем запросы
    results = []
    for query in queries:
        operation, file = query.split()
        if operation in fileAccess.get(file, set()):
            results.append("OK")
        else:
            results.append("Access denied")

    return results


def Main():
    # Считываем количество файлов
    n = int(input())

    # Считываем информацию о файлах и их доступах
    files = [input().split(maxsplit=1) for _ in range(n)]

    # Считываем количество запросов
    m = int(input())

    # Считываем запросы
    queries = [input() for _ in range(m)]

    # Восстанавливаем контроль над правами доступа к файлам
    results = RestoreAccess(files, queries)

    # Выводим результаты
    for result in results:
        print(result)

Main()
