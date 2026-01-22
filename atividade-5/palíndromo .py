def eh_palindromo(texto):
    texto_limpo = ""

    for caractere in texto.lower():
        if caractere.isalnum():  # letras e números
            texto_limpo += caractere

    texto_invertido = texto_limpo[::-1]

    if texto_limpo == texto_invertido:
        return "Sim"
    else:
        return "Não"


frase = input("Digite uma palavra ou frase: ")
print(eh_palindromo(frase))
