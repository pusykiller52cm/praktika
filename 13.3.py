def count_words_starting_with_letter(file_path, letter):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    words = text.split()

    count = sum(1 for word in words if word.lower().startswith(letter.lower()))

    return count


file_path = 'text.txt'
letter = 'р'
result = count_words_starting_with_letter(file_path, letter)
print(f"Количество слов, начинающихся с буквы '{letter}': {result}")