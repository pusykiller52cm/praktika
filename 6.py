from itertools import product

def find_expression():
    # Генерируем все возможные комбинации знаков + и - между цифрами
    for signs in product(['', '+', '-'], repeat=8):
        # Строим выражение, чередуя цифры и знаки
        expression = '1'
        for i, sign in enumerate(signs):
            expression += sign + str(i + 2)
        # Вычисляем значение выражения
        if eval(expression) == 100:
            return expression
    return None

# Пример использования
result = find_expression()
if result:
    print(f"Выражение: {result} = 100")
else:
    print("Решение не найдено.")