def count_max_digits(N):
    # Преобразуем число в строку для удобства работы с цифрами
    digits = str(N)
    # Находим максимальную цифру в числе
    max_digit = max(digits)
    # Считаем количество вхождений максимальной цифры
    count = digits.count(max_digit)
    return count

# Пример использования
N = 1808
result = count_max_digits(N)
print(f"Количество цифр с наибольшим значением в числе {N}: {result}")