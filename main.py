# Домашнее задание по теме "Множественное наследование"

import random


class Animal:
    def __init__(self, speed):
        self.live = True
        self.sound = None
        self._DEGREE_OF_DANGER = 0
        self._cords = [0, 0, 0]  # X, Y, Z
        self.speed = speed

    def move(self, dx, dy, dz):
        # Изменение координат с учетом скорости
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed

        # Обработка координаты Z
        if self._cords[2] + (dz * self.speed) < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] += dz * self.speed

    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        if self.sound is not None:
            print(self.sound)
        else:
            print("Silence")


class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True

    def lay_eggs(self):
        eggs = random.randint(1, 4)
        print(f"Here are(is) {eggs} eggs for you")


class AquaticAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)  # берем модуль
        speed_dive = self.speed / 2  # скорость при нырянии
        self._cords[2] -= dz * speed_dive  # уменьшаем Z
        if self._cords[2] < 0:
            print("It's too deep, i can't dive :(")
            self._cords[2] += dz * speed_dive  # отменяем движение, если глубже нуля


class PoisonousAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self, speed):
        Bird.__init__(self, speed)  # Инициализируем родительские классы
        AquaticAnimal.__init__(self, speed)
        PoisonousAnimal.__init__(self, speed)

        self.sound = "Click-click-click"  # звук утконоса


# Пример использования классов:

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()  # X: 10 Y: 20 Z: 30
db.dive_in(6)
db.get_cords()  # X: 10 Y: 20 Z: 0

db.lay_eggs()  # Here are(is) 3 eggs for you (число может варьироваться)




