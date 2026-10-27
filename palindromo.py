
while True:
    texto = input("Digite o texto (ou 'sair' para encerrar): ")

    if texto.lower()== "sair":
        print("Encerrando o programa. Até logo!")
        break
    texto_limpo = texto.lower().replace(" ", "")
    texto_invertido = texto_limpo[::-1]
    quantidade_letras = len(texto_limpo)

    if texto_limpo == texto_invertido:
        print(f"O texto '{texto}' é um palíndromo! (Ele tem {quantidade_letras} letras)")
    else:
       print(f"O texto '{texto}' não é um palíndromo. (Ele tem {quantidade_letras} letras)")
    