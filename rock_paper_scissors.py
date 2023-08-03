import random

user_points = 0
computer_points = 0

options = ["R", "T", "P"]

while True:
    user_choice = input("Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair: ").upper()

    if user_choice == "Q":
        break

    computer_choice = random.choice(options)

    print("O computador escolheu: " + computer_choice)

    if user_choice == computer_choice:
        print("EMPATE!")

    elif user_choice == "R" and computer_choice == "T":
        print("Você GANHOU!")
        user_points += 1

    elif user_choice == "P" and computer_choice == "R":
        print("Você GANHOU!")
        user_points += 1

    elif user_choice == "T" and computer_choice == "P":
        print("Você GANHOU!")
        user_points += 1

    else:
        print("Você PERDEU!")
        computer_points += 1

print("Sua pontuação: " + str(user_points))
print("Pontuação do Computador: " + str(computer_points))

if computer_points > user_points:
    print("DERROTA!!!!")
elif computer_points == user_points:
    print("EMPATE")
else:
    print("VITÓRIA!!!!")

print("Goodbye!")







