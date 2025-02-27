import math

def calculate_sequence(n):
    sequence = []
    for i in range(1, n+1):
        term = ((-1)**(i-1)) / math.factorial(i)
        sequence.append(term)
    return sequence

def write_to_file(sequence, filename):
    with open(filename, 'w') as file:
        for term in sequence:
            file.write(f"{term}\n")

def print_filtered_terms(filename, epsilon):
    with open(filename, 'r') as file:
        for line in file:
            term = float(line.strip())
            if abs(term) > epsilon:
                print(term)

n = 10
epsilon = 0.01
filename = 'otvet.txt'
sequence = calculate_sequence(n)
write_to_file(sequence, filename)
print_filtered_terms(filename, epsilon)