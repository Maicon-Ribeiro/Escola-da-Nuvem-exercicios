import csv

arquivo = input("Digite o nome do arquivo (ex: pessoas.csv): ")

dados = [
    ["Nome", "Idade", "Cidade"],
    ["Ana", 25, "São Paulo"],
    ["Carlos", 30, "Rio de Janeiro"],
    ["Mariana", 22, "Belo Horizonte"]
]

try:
    with open(arquivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(dados)

    print("Arquivo salvo com sucesso!")

except Exception:
    print("Falha ao salvar o arquivo.")
