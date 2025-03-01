from itertools import permutations

def generate_permutations(numbers):
    return list(permutations(numbers))

# Запрос ввода от пользователя
user_input = input("Введите натуральные числа, разделенные пробелами: ")

# Преобразование введенных данных в список чисел
numbers = list(map(int, user_input.split()))

# Генерация и вывод всех перестановок
all_permutations = generate_permutations(numbers)
print("Все возможные перестановки:")
for perm in all_permutations:
    print(perm)