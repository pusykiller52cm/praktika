def find_smallest_n(epsilon):
    n = 1
    while True:
        a_n = ((-1) ** n) * n / (2 ** n)
        if abs(a_n) < epsilon:
            return n, a_n
        n += 1

# Пример использования
epsilon = 0.01
n, a_n = find_smallest_n(epsilon)
print(f"Наименьший номер n: {n}, a_n: {a_n}")