# Lista apenas com núumeros pares
import time

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 1000000
numeros_pares = []


def for_loop():
    inicio = time.time()
    for num in numeros:
        if num % 2 == 0:
            numeros_pares.append(num)
    fim = time.time()

    print(f"Tempo: {fim - inicio:.4f} segundos")


def list_compre():
    inicio = time.time()
    list_format = [x for x in numeros if x % 2 == 0]

    fim = time.time()
    print(f"Tempo: {fim - inicio:.4f} segundos")


for_loop()
list_compre()

# Tempo de execução do for loop: 0.7198 segundos
# Tempo de execução da List Comprehension:  0.6078 segundos