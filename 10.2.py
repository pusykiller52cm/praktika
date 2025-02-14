def swap_max_with_diagonal(matrix):
    n = len(matrix)
    for i in range(n):
        max_val = max(matrix[i])
        max_index = matrix[i].index(max_val)
        matrix[i][i], matrix[i][max_index] = matrix[i][max_index], matrix[i][i]
    return matrix

# Пример использования
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = swap_max_with_diagonal(matrix)
for row in result:
    print(row)