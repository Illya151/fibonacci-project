def fibonacci(n):
    """Функція для генерації перших n чисел Фібоначчі"""
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence[:n]

if __name__ == "__main__":
    n_terms = 15
    print(f"Перші {n_terms} чисел Фібоначчі:")
    print(fibonacci(n_terms))