def print_vowels(text):
    vowels = {'а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
    found_vowels = sorted([char for char in text if char in vowels])
    print("Гласные буквы в тексте в алфавитном порядке:")
    print(' '.join(found_vowels))

text = int(input("Введите текст:"))
print_vowels(text)