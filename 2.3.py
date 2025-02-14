def is_latin_letter(char):
    # Проверяем, является ли символ латинской буквой
    return char.isalpha() and char.isascii()

# Пример использования
char = 'A'
result = is_latin_letter(char)
print(f"Результат: {result}")