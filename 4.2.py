def calculate_P(a, n):
    product = 1
    for i in range(n + 1):
        product *= (a - i * n)
    return product

# Пример использования
a = 5
n = 3
result = calculate_P(a, n)
print(f"P = {result}")