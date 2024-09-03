#EX 2

def fibonacci(n):
    sequenciaFib = [0, 1]
    while sequenciaFib [-1] < n:
        sequenciaFib.append(sequenciaFib[-1] + sequenciaFib[-2])
    return sequenciaFib

def pertenceFib (n):
    sequenciaFib = fibonacci(n)
    if n in sequenciaFib:
        return f"O número {n} pertence a sequência de Fibonacci."
    else:
        return f"O número {n} não pertence a sequência de Fibonacci."

numero = int(input("Informe um número: "))
resultado = pertenceFib(numero)
print(resultado)
