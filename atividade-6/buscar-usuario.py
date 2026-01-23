import requests

try:
    resposta = requests.get("https://randomuser.me/api/")
    dados = resposta.json()["results"][0]

    nome = dados["name"]["first"]
    email = dados["email"]
    pais = dados["location"]["country"]

    print("Nome:", nome)
    print("Email:", email)
    print("País:", pais)

except:
    print("Falha ao buscar usuário.")
