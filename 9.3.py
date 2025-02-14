def find_common_element(x, y, z):
    i = j = k = 0
    p, q, r = len(x), len(y), len(z)
    
    while i < p and j < q and k < r:
        if x[i] == y[j] == z[k]:
            return x[i]
        elif x[i] < y[j]:
            i += 1
        elif y[j] < z[k]:
            j += 1
        else:
            k += 1
    return None

# Пример использования
x = [1, 2, 4, 6, 8]
y = [2, 3, 6, 7, 9]
z = [2, 6, 10, 12, 15]

common_element = find_common_element(x, y, z)
if common_element:
    print(f"Общее число: {common_element}")
else:
    print("Общего числа нет.")