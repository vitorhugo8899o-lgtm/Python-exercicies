# contador de números
import time

def contador(n: int):
    for numero in range(1, n + 1):
        yield numero

inicio = time.time()

for valor in contador(10000):
    print(valor)

final = time.time()

# list_compre = [valor for valor in contador(10000)]


print(f"Tempo: {final - inicio:.4f} segundos")



# Tempo de execução do loop for: Tempo: 0.6909 segundos
# TEmpo de execução da list comprehension: Tempo: 0.0008 segundos

# number = contador(10000)

# # Visualização dos números sendo processados 1 de cada vez
# print(next(number))  # 1
# print(next(number))  # 2 
# print(next(number))  # 3
# print(next(number))  # 4
