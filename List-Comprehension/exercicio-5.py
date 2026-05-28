#Multiplos Filtros

produtos = [
    ("Smartphone X", 15, "Eletrônicos", 1200.0),
    ("Cadeira Gamer", 5, "Móveis", 350.0),
    ("Aspirador de Pó", 0, "Eletrodomésticos", 400.0),
    ("Fone Bluetooth", 50, "Eletrônicos", 150.0),
    ("Mesa de Escritório", 3, "Móveis", 600.0),
    ("Geladeira Smart", 2, "Eletrodomésticos", 2500.0),
    ("Monitor Ultrawide", 0, "Eletrônicos", 1100.0),
    ("Livro de Python", 100, "Livros", 80.0)
]

produtos_tributados = [
    (nome, preco_base * 1.15 if preco_base > 500 else preco_base * 1.10)  
    for nome,estoque,categoria,preco_base in produtos
    if categoria in ['Eletrodomésticos', 'Eletrônicos']
    and estoque > 0
]

print(produtos_tributados)