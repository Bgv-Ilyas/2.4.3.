#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import cmath

class Pair(ABC):
    @abstractmethod
    def add(self, other):
        pass

    @abstractmethod
    def subtract(self, other):
        pass

    @abstractmethod
    def multiply(self, other):
        pass

    @abstractmethod
    def divide(self, other):
        pass

    @abstractmethod
    def input(self):
        pass

    @abstractmethod
    def output(self):
        pass

class FuzzyNumber(Pair):
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def add(self, other):
        return FuzzyNumber(self.lower + other.lower, self.upper + other.upper)

    def subtract(self, other):
        return FuzzyNumber(self.lower - other.lower, self.upper - other.upper)

    def multiply(self, other):
        return FuzzyNumber(self.lower * other.lower, self.upper * other.upper)

    def divide(self, other):
        if other.lower == 0 or other.upper == 0:
            raise ValueError("Деление на ноль невозможно")
        return FuzzyNumber(self.lower / other.upper, self.upper / other.lower)

    def input(self):
        self.lower = float(input("Введите нижнюю границу: "))
        self.upper = float(input("Введите верхнюю границу: "))

    def output(self):
        print(f"Нечеткое число: [{self.lower}, {self.upper}]")

class Complex(Pair):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def subtract(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def multiply(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def divide(self, other):
        if other.real == 0 and other.imag == 0:
            raise ValueError("Деление на ноль невозможно")
        denom = other.real ** 2 + other.imag ** 2
        return Complex((self.real * other.real + self.imag * other.imag) / denom,
                       (self.imag * other.real - self.real * other.imag) / denom)

    def input(self):
        self.real = float(input("Введите действительную часть: "))
        self.imag = float(input("Введите мнимую часть: "))

    def output(self):
        print(f"Комплексное число: {self.real} + {self.imag}i")

def demonstrate_virtual_call(pair):
    pair.output()

def main():
    # Демонстрация работы с нечеткими числами
    fuzzy1 = FuzzyNumber(1.0, 2.0)
    fuzzy2 = FuzzyNumber(3.0, 4.0)
    result = fuzzy1.add(fuzzy2)
    demonstrate_virtual_call(result)

    # Демонстрация работы с комплексными числами
    complex1 = Complex(1.0, 2.0)
    complex2 = Complex(3.0, 4.0)
    result = complex1.add(complex2)
    demonstrate_virtual_call(result)

    # Демонстрация ввода и вывода для FuzzyNumber
    fuzzy3 = FuzzyNumber(0, 0)
    fuzzy3.input()
    fuzzy3.output()

    # Демонстрация ввода и вывода для Complex
    complex3 = Complex(0, 0)
    complex3.input()
    complex3.output()

if __name__ == "__main__":
    main()
