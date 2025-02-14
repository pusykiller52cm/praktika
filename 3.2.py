def compare_numbers(a, b, c, d):
    if a == d:
        return "a равно d"
    elif b == d:
        return "b равно d"
    elif c == d:
        return "c равно d"
    else:
        max_diff = max(d - a, d - b, d - c)
        return f"Ни одно из чисел не равно d. Максимальная разность: {max_diff}"

# Пример использования
a = 5
b = 10
c = 15
d = 12

result = compare_numbers(a, b, c, d)
print(result)