def count_elements_above(sequence, znach):
    count = 0
    for row in sequence:
        for element in row:
            if element > znach:
                count += 1
    return count

# Пример использования
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
znach = 5
result = count_elements_above(A, znach)
print(f"Количество элементов, превышающих {znach}: {result}")