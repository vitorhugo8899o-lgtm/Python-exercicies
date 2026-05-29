# Contador de números pares
import time


def pares(limite: int):
    for numero in range(1, limite+1):
        if numero % 2 == 0:
            yield numero

inicio = time.time()

for valor in pares(10000):
    print(valor)

final = time.time()

print(f"Tempo: {final - inicio:.4f} segundos")



# inicio = time.time()
# list_compre = [valor for valor in pares(10000)]
# final = time.time()


# print(list_compre)

# Tempo de execução no loop for: Tempo: 0.3842 segundos
# Tempo de execução na list_comprehension: Tempo: 0.0010 segundos
