import math

R = float(input("Введите радиус круга R: "))

C = 2 * math.pi * R

A = math.pi * R ** 2

print(f"Длина окружности: {C:.42f}")
print(f"Площадь круга: {A:.42f}")