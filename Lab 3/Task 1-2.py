import math


class Shape:
    def __init__(self, identifier):
        if not isinstance(identifier, str):
            raise TypeError("Идентификатор должен быть строкой")
        self.identifier = identifier

    def move(self, dx, dy):
        raise NotImplementedError("Метод move должен быть переопределен в подклассах")

    def is_include(self, x, y):
        raise NotImplementedError("Метод is_include должен быть переопределен в подклассах")


class Rectangle(Shape):
    def __init__(self, identifier, width, height, x=0, y=0):
        super().__init__(identifier)
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Ширина и высота должны быть числами")
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def move(self, dx, dy):
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError("Смещение должно быть числом")
        self.x += dx
        self.y += dy

    def is_include(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Координаты точки должны быть числами")
        return (self.x <= x <= self.x + self.width) and (self.y <= y <= self.y + self.height)


class Pentagon(Shape):
    def __init__(self, identifier, side_length, x=0, y=0):
        super().__init__(identifier)
        if not isinstance(side_length, (int, float)):
            raise TypeError("Длина стороны должна быть числом")
        self.side_length = side_length
        self.x = x
        self.y = y

    def move(self, dx, dy):
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError("Смещение должно быть числом")
        self.x += dx
        self.y += dy

    def is_include(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Координаты точки должны быть числами")
        # Проверяем, попадает ли точка внутрь пятиугольника
        angle = 2 * math.pi / 5
        cx, cy = self.x + self.side_length, self.y + self.side_length
        for i in range(5):
            x1 = self.x + self.side_length * math.cos(i * angle)
            y1 = self.y + self.side_length * math.sin(i * angle)
            x2 = self.x + self.side_length * math.cos((i + 1) * angle)
            y2 = self.y + self.side_length * math.sin((i + 1) * angle)
            if ((y1 <= y and y < y2) or (y2 <= y and y < y1)) and x > (x2 - x1) * (y - y1) / (y2 - y1) + x1:
                return True
            cx, cy = x2, y2
        return False


# Пример использования классов
if __name__ == "__main__":
    try:
        # Создаем объекты Прямоугольник и Пятиугольник
        rectangle = Rectangle("rect1", 5, 10)
        pentagon = Pentagon("pent1", 7)

        # Перемещаем объекты
        rectangle.move(2, 3)
        pentagon.move(1, -1)

        # Проверяем, входит ли точка в объекты
        print(rectangle.is_include(4, 6))  # Должно быть True
        print(pentagon.is_include(2, 2))  # Должно быть False
    except TypeError as e:
        print("Ошибка типа данных:", e)
    except Exception as e:
        print("Произошла непредвиденная ошибка:", e)
