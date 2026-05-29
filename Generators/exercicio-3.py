# Valor quadrado de um número
import time

def quadrados(lista: list):
    for n in lista:
        yield n ** 2


list_num = [2, 4, 6, 8, 10, 12, 18, 32, 64, 128, 340, 255, 895, 1000, 3000, 5000, 10000]


inicio = time.time()
for valor in quadrados(list_num):
    print(valor)
final = time.time()


# list_compre = [valor for valor in quadrados(list_num)]

print(f"Tempo: {final - inicio:.4f} segundos")


# Tempo de execução do loop for: Tempo: 0.0015 segundos
# Tempo de execução da list comprehension: Tempo: 0.0000 segundos
