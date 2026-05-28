#Transforma lista de palavras em minúsculas em maiúsculas
import time

palavras = ["python", "codigo", "pratica", "dados"]  * 1000000
palavras_maiusculas = []

def for_loop():
    inicio = time.time()
    for palavra in palavras:
        palavras_maiusculas.append(palavra.upper())
    
    fim = time.time()

    print(f"Tempo: {fim - inicio:.4f} segundos")


def list_compre():
    inicio = time.time()
    palavras_maiusculas_format = [palavra.upper() for palavra in palavras]

    fim = time.time()

    print(f"Tempo: {fim - inicio:.4f} segundos")


for_loop()
list_compre()

#Tempo de execução: 
# loop for normal:0.4954 segundos
# List Comprehension: Tempo: 0.3873 segundos