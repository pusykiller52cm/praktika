import math

def calculate_formulas(x, y):
    formula1 = 3**x - 4*x + (y - math.sqrt(abs(x)))
    formula2 = 2**(-x) - math.cos(x) + math.sin(2*x*y)
    return formula1, formula2
x = int(input("Введите первое число:"))
y = int(input("Введите второе число:"))
result1, result2 = calculate_formulas(x, y)
print(f"Результат первой формулы: {result1}")
print(f"Результат второй формулы: {result2}")