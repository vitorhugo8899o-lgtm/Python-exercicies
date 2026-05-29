# Sequência de Fibonacci
import time

def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b


inicio = time.time()

for valor in fibonacci(10000):
    print(valor)

final = time.time()


# list_compre = [valor for valor in fibonacci(10000)]



print(f"Tempo: {final - inicio:.4f} segundos")

#Tempo de execução do loop for: Tempo: 1.7227 segundos
# TEmpo de execução da list comprehension: Tempo: 0.0064 segundos
