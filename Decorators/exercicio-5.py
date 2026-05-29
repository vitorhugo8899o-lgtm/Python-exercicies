




def repetir(vezes=3):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(vezes):
                func(*args, **kwargs)

        return wrapper
    return decorador


@repetir()
def bip():
    print("Bip!")


print(bip())