# Filtrar dados


vendas = [
    ("NFX-101", 150.0, "concluido"),
    ("NFX-102", 450.0, "cancelado"),
    ("NFX-103", 300.0, "concluido"),
    ("NFX-104", 50.0,  "concluido"),
    ("NFX-105", 600.0, "pendente"),
    ("NFX-106", 120.0, "concluido"),
    ("NFX-107", 250.0, "concluido")
]

vendas_processadas = [
    (codigo, valor * 0.9 if valor > 200 else valor)
    for codigo, valor, status in vendas
    if status == "concluido"
]

print(vendas_processadas)