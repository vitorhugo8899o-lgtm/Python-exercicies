
def apenas_positivos(func):
    def verificar(*args, **kwargs):
        if not all(n > 0 for n in args):
            return "Acesso negado: números negativos não são permitidos."

        return func(*args, **kwargs)

    return verificar


@apenas_positivos
def multiplicar_tres_numeros(a, b, c):
    return a * b * c


print(multiplicar_tres_numeros(10, 2, 3))
print(multiplicar_tres_numeros(5, 2, -1))