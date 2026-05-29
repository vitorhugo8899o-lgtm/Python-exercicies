# Converter minúsculas para maiúsculas

def caixa_alta(func):
    def maiuscula(*args, **kwargs):
        st = func(*args, **kwargs)
        return st.upper()
    return maiuscula


@caixa_alta
def obter_mensagem(frase: str):
    return frase.lower()


print(obter_mensagem('pytHOn'))