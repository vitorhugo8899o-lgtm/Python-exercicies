# Pipeline de Dados

list_str = [
    'Python para análise de dados',
    "Vamos jogar CS2",
    "Estrutura de dados",
    "FastAPI Love you",
    "Ano atual 2026"
]


def leitor_textos(lista_frases: list):
    for frase in lista_frases:
        yield frase



def filtro_palavra(generator, palavra: str):
    for frase in generator:
        if palavra.lower() in frase.lower():
            yield frase



for st in filtro_palavra(leitor_textos(list_str), "FastAPI"):
    print(st)
