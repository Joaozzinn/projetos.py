print('OLÁ, BEM-VINDO AO QUIZ DO JOÃO!');

score = 0

quiz = str(input('Está pronto? (S/N)')).strip().upper();

if quiz != "S":
    quit();


print('Processando...');

##############################################################################################################################################################################
print('*=*' * 20);


print('01. Qual foi a empresa que desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Rockstar Games \n (B) Ubisoft \n (C) EA \n (D) Activision \n ');


respota_01 = str(input('RESPOSTA: ')).strip().upper();


if respota_01 == "A":
    print('CORRETO!');
    score = score + 1

else:
    print('INCORRETO!');

print('*=*' * 20);
##############################################################################################################################################################################

print('Proxima pergunta:')
print('02.Como é o nome do protagonista de GTA San Andreas? \n (A) Carlos Jonh \n (B) Carl Jonhson \n (C) Carl jack \n (D) Carlos Jonhson \n ');

respota_02 = str(input('RESPOSTA: ')).strip().upper(); 


if respota_02 == "B":
    print('CORRETO!');
    score = score + 1

else:
    print('INCORRETO!');


print('*=*' * 20);

##############################################################################################################################################################################

print('Proxima pergunta:');
print('Um pouco mais complicada essa...');
print('03.Qual é o código do carro voador (GTA SAN ANDREAS)? \n (A) RIPAZHA \n (B) HIJUTYH \n (C) FGHTJKI \n (D) CARVOADOR \n');

respota_03 = str(input('RESPOSTA: ')).strip().upper();


if respota_03 == "A":
    print('CORRETO!');
    score = score + 1

else:
    print('INCORRETO!')

print('*=*' * 20);
##############################################################################################################################################################################

print('Proxima...');
print('04.No jogo God Of War ( Deus Da Guerra ), quem é considerado o Deus da água? \n (A) Poseidon \n (B) Ades \n (C) Kratos \n (D)Thor \n')


resposta_04 = str(input('RESPOSTA: ')).strip().upper();


if resposta_04 == "A":
    print('CORRETO!');
    score = score + 1

else:
    print('INCORRETO!');

print('*=*' * 20)

##############################################################################################################################################################################


print('Proxima...')
print('05.Qual é o nome do filho de Kratos em God of War? \n (A) Ares \n (B) Apollo \n (C) Hermes \n (D) Atreus \n');


resposta_05 = str(input('RESPOSTA: ').strip().upper());


if resposta_05 == "D":
    print('CORRETO!');
    score = score + 1

else:
    print('INCORRETO!');

print('*=*' * 20);

##################################################################################################################################################################################


print('Proxima...');
print('06.Qual é o artefato principal usado por Kratos em God of War (2018)? \n (A)Leviatã \n (B) Mjolnir \n (C) Espada de Ébano \n (D)Lâmina do Caos \n');


resposta_06 = str(input('RESPOSTA: ')).strip().upper();


if resposta_06 == "A":
    print('CORRETO!')
    score = score + 1;

else:
    print('INCORRETO!');





##############################################################################################################################################################################
print(f'O QUIZ FINALIZOU... PONTUAÇÃO: {score}/6')
##############################################################################################################################################################################
