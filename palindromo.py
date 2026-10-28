print("Bem-vindo M-Monteiro-prog! esse é o seu verificador de palíndromos!")
print("Digite 'sair' a qualquer momento para encerrar o programa.")

historico_de_palavras = []
palavras_não_palindromas = []
palavras_palindromas = []

while True:
    texto = input("Digite o texto (ou 'sair' para encerrar): ")

    if texto.lower()== "sair":
        print(f"Você testou {len(historico_de_palavras)} palavras no total.")
        print("Palavras testadas:")
        for item in historico_de_palavras:
            print(f"- {item}")

        print("Palavras palíndromas:")
        for item in palavras_palindromas:
            print(f"- {item}")

        print("Palavras não palíndromas:")
        for item in palavras_não_palindromas:
            print(f"- {item}")

        print("Encerrando o programa. Até logo!")
        break

    historico_de_palavras.append(texto)

    texto_limpo = texto.lower().replace(" ", "")
    texto_invertido = texto_limpo[::-1]
    quantidade_letras = len(texto_limpo)

    if texto_limpo == texto_invertido:
        palavras_palindromas.append(texto)
        print(f"O texto '{texto}' é um palíndromo! (Ele tem {quantidade_letras} letras)")
    else:
        palavras_não_palindromas.append(texto)
        print(f"O texto '{texto}' não é um palíndromo. (Ele tem {quantidade_letras} letras)")
