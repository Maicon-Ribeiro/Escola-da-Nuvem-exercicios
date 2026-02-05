import pandas as pd

arquivo = input("Digite o nome do arquivo CSV: ")

try:
    df = pd.read_csv(arquivo)

    media = df["tempo_execucao"].mean()
    desvio = df["tempo_execucao"].std()

    print("Média do tempo_execucao:", media)
    print("Desvio padrão:", desvio)

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
except Exception as e:
    print("Erro ao ler o arquivo:", e)
