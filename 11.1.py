def count_abc_occurrences(s):
    return s.count("abc")

# Пример использования
s = "abcabcabcxyzabc"
count = count_abc_occurrences(s)
print(f"Группа букв 'abc' входит в строку {count} раз(а)")