"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores
anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado
pertence ou não a sequência.
"""


def fibonacci(n):
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence


def in_fibonacci(n):
    fibonacci_sequence = fibonacci(n)
    if n in fibonacci_sequence:
        return True
    else:
        return False


number = int(input("Digite um número: "))
if in_fibonacci(number):
    print(f"O número {number} pertence a Fibonacci.")
else:
    print(f"O número {number} não pertence a Fibonacci.")
