# Dict Comprehensions.

dados_usuarios = [
    ("123.456.789-00", "Carlos", "admin"),
    ("987.654.321-11", "Juliana", "user"),
    ("555.666.777-88", "Roberto", "visitante")
]


usuarios_anonimos = {
    cpf[:3] + '.***.***-**': (
        f"{nome} ({role.upper()})"
    )
    for cpf, nome, role in dados_usuarios
    if role in ['admin', 'user']
}

print(usuarios_anonimos)
