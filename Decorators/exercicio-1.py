# Decorators


def avisar_execucao(func):
    def avisar():
        print('Iniciando a função...')
        func()
        print('Função finalizada!')
    return avisar


@avisar_execucao
def ola_mundo():
    print('Olá, mundo!')


ola_mundo()