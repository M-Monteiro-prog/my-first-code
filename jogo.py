import random


numero_secreto = random.randint(1, 100)
tentativas = 0

print("Olá, M-Monteiro-prog! Bem-vindo ao seu jogo avançado em Python!")
print("Eu pensei em um número entre 1 and 100. Você consegue adivinhar?")

while True:
    chute = int(input("Digite o seu palpite: "))
    tentativas += 1
    
    if chute == numero_secreto:
        print(f"\nParabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
        
        # Sistema de mensagens personalizadas baseadas no desempenho
        if tentativas <= 5:
            print("🏆 Impressionante! Você tem mente de hacker ou leu meu código? Gênio!")
        elif tentativas <= 8:
            print("⚡ Muito bom! Sua estratégia de busca matemática foi excelente.")
        elif tentativas <= 12:
            print("👍 Bom trabalho! Ficou dentro da média esperada para 100 números.")
        else:
            print("😅 Demorou um pouquinho, hein? Na próxima você consegue melhorar a estratégia!")
            
        break  # Encerra o jogo
    elif chute < numero_secreto:
        print(f"O número {chute} é muito baixo! Tente um número maior.")
    else:
        print(f"O número {chute} é muito alto! Tente um número menor.")
