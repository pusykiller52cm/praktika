def calculate_F(x):
    if x > 3:
        return -3 * x + 9
    else:
        return (x ** 3) / (x ** 2 + 8)

# Пример использования
x = 2
result = calculate_F(x)
print(f"F({x}) = {result}")

x = 4
result = calculate_F(x)
print(f"F({x}) = {result}")