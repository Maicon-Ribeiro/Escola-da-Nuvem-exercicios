def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta


# Exemplo de uso
valor = float(input("Digite o valor da conta: "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))

resultado = calcular_gorjeta(valor, porcentagem)
print("Valor da gorjeta: R$", resultado)
