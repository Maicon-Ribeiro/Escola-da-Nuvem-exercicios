import requests

moeda = input("Digite a moeda (ex: USD, EUR): ").upper()

try:
    resposta = requests.get(f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL")
    dados = resposta.json()[f"{moeda}BRL"]

    print("Valor atual:", dados["bid"])
    print("Máxima:", dados["high"])
    print("Mínima:", dados["low"])
    print("Última atualização:", dados["create_date"])

except:
    print("Erro ao consultar a moeda.")
