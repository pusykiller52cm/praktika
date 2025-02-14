def filter_numbers_ending_with_k(arr, k):
    return [x for x in arr if x % 10 == k]

# Пример использования
arr = [123, 456, 789, 12, 34, 56]
k = 6
new_arr = filter_numbers_ending_with_k(arr, k)
print(f"Новый массив: {new_arr}")