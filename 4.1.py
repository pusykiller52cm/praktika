def sum_of_n_digit_numbers(n, k):
    start = 10 ** (n - 1)
    end = 10 ** n
    total_sum = sum(i for i in range(start, end) if i % k == 0)
    return total_sum

# Пример использования
n = 2
k = 3
result = sum_of_n_digit_numbers(n, k)
print(f"Сумма всех {n}-значных чисел, кратных {k}: {result}")