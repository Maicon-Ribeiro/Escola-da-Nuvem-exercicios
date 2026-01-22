preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto: "))

valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto

preco_final = round(preco_final, 2)

print("Preço final com desconto: R$", preco_final)
