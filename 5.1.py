def sum_first_last_digit(n):
    # Преобразуем число в строку для удобства работы с цифрами
    digits = str(n)
    first_digit = int(digits[0])
    last_digit = int(digits[-1])
    return first_digit + last_digit

# Пример использования
n = 12345
result = sum_first_last_digit(n)
print(f"Сумма первой и последней цифр числа {n}: {result}")