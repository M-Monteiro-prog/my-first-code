import random
numero_secreto = random.randint(1, 10)
tentativas = 0
print("Olá, M-Monteiro-prog! Bem-vindo...")
while True:
  chute = int(input("Digite seu palpite: "))
  tentativas += 1
  if chute == numero_secreto:
    print(f"Parabéns! Você acertou em {tentativas} tentativas!")
    break
  elif chute < numero_secreto:
    print("Muito baixo! Tente um número maior.")
  else:
    print("Muito alto! Tente um número menor.")
