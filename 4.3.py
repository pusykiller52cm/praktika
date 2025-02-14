import math

def calculate_F(x):
    return 2 * math.cos(math.sqrt(x)) + 0.5

def print_function_table(a, b, h):
    print("x\tF(x)")
    x = a
    while x <= b:
        print(f"{x:.2f}\t{calculate_F(x):.4f}")
        x += h

# Пример использования
a = 1
b = 10
h = 1
print_function_table(a, b, h)