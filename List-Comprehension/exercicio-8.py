# Iterando sobre um dicionário existente


produtos_atuais = {
    "Teclado": 120.0,
    "Mouse": 80.0,
    "Monitor": 900.0,
    "Tapete Mouse": 30.0
}


catalogo_reajustado = {
    nome.lower(): (
        preco * 0.85
        if preco > 200
        else preco
    )
    for nome, preco in produtos_atuais.items()
    if preco >= 50.0
}

print(catalogo_reajustado)
