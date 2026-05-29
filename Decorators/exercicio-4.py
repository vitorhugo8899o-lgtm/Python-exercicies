# Multiplos decoradores


def negrito(func):
    def aplicar():
        return f"<b>{func()}<b/>"
    return aplicar


def italico(func):
    def aplicar():
        return f"<i>{func()}<i/>"
    return aplicar


@negrito
@italico
def ola():
    return "Olá"


print(ola())