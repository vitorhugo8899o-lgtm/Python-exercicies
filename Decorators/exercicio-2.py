# Dobrar a soma

def dobrar_resultado(func):
    def dobrar(*args, **kwargs):
        result = func(*args, **kwargs) * 2
        return result
    return dobrar


@dobrar_resultado
def somar(n1, n2):
    return n1 + n2


print(somar(10, 5))