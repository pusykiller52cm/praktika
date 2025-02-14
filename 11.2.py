def hamming_distance(word1, word2):
    return sum(c1 != c2 for c1, c2 in zip(word1, word2))

def find_max_distance_pair(sentence, length):
    words = [word for word in sentence.split() if len(word) == length]
    max_distance = 0
    pair = (None, None)
    
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            distance = hamming_distance(words[i], words[j])
            if distance > max_distance:
                max_distance = distance
                pair = (words[i], words[j])
    
    return pair, max_distance

# Пример использования
sentence = "hello world hello earth"
length = 5
pair, distance = find_max_distance_pair(sentence, length)
print(f"Пара слов с максимальным расстоянием: {pair}, расстояние: {distance}")