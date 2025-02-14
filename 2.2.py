def swap_integer_fractional_parts(number):
    # Разделяем число на целую и дробную части
    integer_part = int(number)
    fractional_part = int((number - integer_part) * 1000)
    
    # Меняем местами и формируем новое число
    new_number = fractional_part + integer_part / 1000
    return new_number

# Пример использования
R = 123.456
new_R = swap_integer_fractional_parts(R)
print(f"Новое число: {new_R}")