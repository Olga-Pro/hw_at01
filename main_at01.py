def remainder(a, b):  # ДЗ
    if b == 0:
        raise ValueError("Делитель не может быть = 0.")
    return a % b

# Из урока:
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError('На ноль делить нельзя')
    return a / b


def check(number):
    return number % 2 == 0
