arquivo = input("Digite o nome do arquivo: ")

try:
    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            print(linha.strip())

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
