def calculate_average(matrix, R, S):
    n = len(matrix)
    m = len(matrix[0]) if n > 0 else 0
    total = 0
    count = 0
    for i in range(R - 1, n, R):
        for j in range(S - 1, m, S):
            total += matrix[i][j]
            count += 1
    return total / count if count > 0 else 0

# Пример использования
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

R = 2
S = 2
average = calculate_average(matrix, R, S)
print(f"Среднее арифметическое: {average}")