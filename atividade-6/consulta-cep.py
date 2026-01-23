import requests

cep = input("Digite o CEP: ")

try:
    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    dados = resposta.json()

    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        print("Logradouro:", dados["logradouro"])
        print("Bairro:", dados["bairro"])
        print("Cidade:", dados["localidade"])
        print("Estado:", dados["uf"])

except:
    print("Erro na requisição.")
