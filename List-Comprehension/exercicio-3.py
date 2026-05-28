# Calcular o dobro
import time

valores = [5, 10, 15, 20, 25] * 1000000
valores_dobrados = []


print(valores_dobrados)


def for_loop():
    inicio = time.time()
    for valor in valores:
        valores_dobrados.append(valor * 2)
    fim = time.time()

    print(f"Tempo: {fim - inicio:.4f} segundos")


def list_compre():
    inicio = time.time()
    list_format = [valor * 2 for valor in valores]
    fim = time.time()

    print(f"Tempo: {fim - inicio:.4f} segundos")


for_loop()
list_compre()

# Tempo de execução do for loop:  0.4265 segundos
# Tempo de execução da List Comprehension:  0.2776 segundos
