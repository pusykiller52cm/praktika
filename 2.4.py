def is_point_in_shaded_area(x, y):
    # Проверяем, принадлежит ли точка кругу с центром в (0, 0) и радиусом 5
    return x**2 + y**2 <= 25

# Пример использования
x = 3
y = 4
result = is_point_in_shaded_area(x, y)
print(f"Результат: {result}")