import re

def remove_duplicate_words(text):
    # Разделяем текст на предложения
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    edited_sentences = []
    for sentence in sentences:
        words = sentence.split()
        unique_words = []
        for word in words:
            if not unique_words or word.lower() != unique_words[-1].lower():
                unique_words.append(word)
        edited_sentences.append(' '.join(unique_words))
    
    return ' '.join(edited_sentences)

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    edited_text = remove_duplicate_words(text)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(edited_text)

# Пример использования
input_file = 'input.txt'  # Укажите путь к исходному файлу
output_file = 'output.txt'  # Укажите путь к выходному файлу
process_file(input_file, output_file)
