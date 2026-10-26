texto = "vscode" 
texto_limpo = texto.lower().replace(" ","")
texto_invertido = texto_limpo[::-1]
if texto_limpo == texto_invertido:
    print(f"O texto '{texto}' é um palíndromo!")
else:
    print(f"O texto '{texto}' não é um palíndromo.")