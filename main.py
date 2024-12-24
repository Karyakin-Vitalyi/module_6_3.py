# Дополнительное практическое задание по модулю: "Наследование классов."

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = list(color)  # RGB color as a list
        self.filled = False

        # Если количество сторон верное, устанавливаем их
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def get_perimeter(self):
        return sum(self.__sides)  # Это будет просто сумма всех сторон


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color, 1)  # одна сторона
        self.__radius = circumference / (2 * 3.14159)  # Получаем радиус из длины окружности

    def get_square(self):
        return 3.14159 * (self.__radius ** 2)

    def get_radius(self):
        return self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)  # Наследуем все атрибуты от Figure

    def get_square(self):
        a, b, c = self.__sides
        s = (a + b + c) / 2  # Полупериметр
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Формула Герона


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        super().__init__(color, *([side] * self.sides_count))  # 12 сторон с указанным значением

    def get_volume(self):
        return self.get_sides()[0] ** 3  # Объём куба V = a^3


# Примеры использования:

circle1 = Circle((200, 200, 100), 10)  # (Цвет, длина окружности)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)
print(circle1.get_color())

cube1.set_color(300, 70, 15)
print(cube1.get_color())
# Проверка на изменение сторон:
print(cube1.get_sides())

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга):
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())





