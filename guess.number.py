import random;


print("Seja muito bem vindo ao guess Number do João!");

choice_number = input('Digite o número teto do desafio: ');


if choice_number.isdigit():
    choice_number = int(choice_number);

else:
    print("Erro: valor informado não é numérico. Favor execute novamente e informe um número!")
    quit();
    
random_number = random.randint(0, choice_number);

n_choices = 0

while True:
    answer_user = input("Adivinhe o número: ")

    if answer_user.isdigit():
        answer_user = int(answer_user);

    else:
        print("Erro: valor informado não é numérico. Favor execute novamente e informe um número!")
        continue


    n_choices = n_choices + 1
    if answer_user == random_number:
        print("ACERTOU!")
        break

    elif answer_user > random_number:
        print("CHUTOU ALTO, o número randomico é menor que isso...");
 
    else:
        print("CHUTO BAIXO, o número randomuco é maior que isso...");


print(f"N° de tentativas: {n_choices}");

