# 1. Pedir o nome do usuário
# 2. Pedir o ano em que o usuário nasceu
# 3. Calcular a idade (Ano atual - Ano de nascimento)
# 4. Mostrar o resultado na tela
from datetime import date

print("--- Calculadora de Idade Avançada ---")

# Pega a data de hoje direto do sistema do computador
hoje = date.today()

# Coleta os dados de nascimento
ano_nasc = int(input("Digite o ano em que você nasceu: "))
mes_nasc = int(input("Digite o mês em que você nasceu (número): "))
dia_nasc = int(input("Digite o dia em que você nasceu: "))

# Cria um objeto de data com o nascimento
data_nascimento = date(ano_nasc, mes_nasc, dia_nasc)

# Calcula a diferença exata em dias entre hoje e o nascimento
dias_vividos = (hoje - data_nascimento).days

# Descobre os anos completos
anos = dias_vividos // 365
dias_restantes = dias_vividos % 365
meses = dias_restantes // 30
dias = dias_restantes % 30

print("\nResultado:")
print(f"Você já viveu cerca de {anos} anos, {meses} meses e {dias} dias!")
print(f"(Isso dá um total de {dias_vividos} dias de muita história!)")