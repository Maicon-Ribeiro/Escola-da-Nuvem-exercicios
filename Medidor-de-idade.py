idade = int(input("Digite sua idade: "))

if 0 <= idade <= 12:
    print("Criança")
elif 13 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 29:
    print("Adulto")
elif idade >= 60:
    print("Idoso")
else:
    print("Faixa etária não definida")
