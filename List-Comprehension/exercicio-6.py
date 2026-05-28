# Dict Comprehensions.

usuarios = [
    ("ana", 25, "Ativo"),
    ("beatriz", 17, "Inativo"),
    ("caio", 32, "Ativo"),
    ("daniel", 16, "Ativo"),
    ("eduardo", 19, "Inativo")
]

painel_controle = {
    nome.title(): (
        "Acesso Permitido"
        if idade >= 18
        else "Acesso Bloqueado"
    )
    for nome, idade, status in usuarios
    if status == "Ativo"
}


print(painel_controle)
