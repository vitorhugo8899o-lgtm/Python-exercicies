#Processamento e Filtro

alunos_notas = [
    ("Paula", [8.5, 9.0, 7.5]),
    ("Lucas", [5.0, 6.5, 4.0]),
    ("Beatriz", [9.5, 10.0, 9.0]),
    ("Rodrigo", [6.0, 7.0, 8.0])
]

alunos_aprovados = {
    nome: (
        sum(notas) / len(notas)
    )
    for nome, notas in alunos_notas
    if sum(notas) / len(notas) >= 7
}

print(alunos_aprovados)