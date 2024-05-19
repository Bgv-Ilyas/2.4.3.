#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

class Triad:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def set_values(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def sum(self):
        return self.a + self.b + self.c

class Triangle(Triad):
    def __init__(self, a=0, b=0, c=0):
        super().__init__(a, b, c)
        if not self.is_valid_triangle():
            raise ValueError("Стороны не образуют треугольник")

    def is_valid_triangle(self):
        return (self.a + self.b > self.c and 
                self.a + self.c > self.b and 
                self.b + self.c > self.a)

    def area(self):
        # Формула Герона
        s = self.sum() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def angles(self):
        # Формула косинусов для нахождения углов
        angle_a = math.acos((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c))
        angle_b = math.acos((self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c))
        angle_c = math.acos((self.a**2 + self.b**2 - self.c**2) / (2 * self.a * self.b))
        return (math.degrees(angle_a), math.degrees(angle_b), math.degrees(angle_c))

def main():
    # Демонстрация возможностей класса Triad
    triad = Triad(3, 4, 5)
    print(f"Триада чисел: {triad.a}, {triad.b}, {triad.c}")
    print(f"Сумма чисел в триаде: {triad.sum()}")

    # Демонстрация возможностей класса Triangle
    triangle = Triangle(3, 4, 5)
    print(f"\nТреугольник со сторонами: {triangle.a}, {triangle.b}, {triangle.c}")
    print(f"Площадь треугольника: {triangle.area():.2f}")

    angles = triangle.angles()
    print(f"Углы треугольника: {angles[0]:.2f}°, {angles[1]:.2f}°, {angles[2]:.2f}°")

    # Попытка создания недопустимого треугольника
    try:
        invalid_triangle = Triangle(1, 1, 3)
    except ValueError as e:
        print(f"\nОшибка при создании треугольника: {e}")

if __name__ == "__main__":
    main()
