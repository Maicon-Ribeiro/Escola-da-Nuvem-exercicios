import json

arquivo = "dados.json"
pessoas = []

try:
    quantidade = int(input("Quantas pessoas deseja cadastrar? "))

    for i in range(quantidade):
        print(f"\nPessoa {i+1}")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        cidade = input("Cidade: ")

        pessoas.append({
            "nome": nome,
            "idade": idade,
            "cidade": cidade
        })

    # Salvar JSON
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(pessoas, f, ensure_ascii=False, indent=4)

    print("\nArquivo salvo com sucesso!")

    # Ler JSON
    with open(arquivo, "r", encoding="utf-8") as f:
        dados_lidos = json.load(f)

    print("\nDados salvos:")
    for pessoa in dados_lidos:
        print(pessoa)

except Exception:
    print("Erro ao salvar ou ler o arquivo.")
