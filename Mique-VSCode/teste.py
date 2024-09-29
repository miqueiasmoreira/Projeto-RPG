from random import randint
import os
from time import sleep

# Status do personagem

vida = 0
defesa = 0
forca = 0
esgrima = 0
adestramento = 0
magia = 0
furtividade = 0
mineracao = 0
ferreiro = 0

# Status - Lobo Selvagem

loboDano = 5
loboVida = 50

print('\033[1;32m-=\033[m' * 10)
print('\033[1;35mCrie seu personagem\033[m')
print('\033[1;32m-=\033[m' * 10)

print('''Raças disponíveis:

Humano [0]
Elfo [1]
Anão [2]
''')

escolhaRaca = int(input('Escolha: ').strip())

# Resultado da escolha da raça

if escolhaRaca == 0:
    print('Raça escolhida, "Humano"')
    vida = 20
    defesa = 10
    forca = 30
elif escolhaRaca == 1:
    print('Raça escolhida, "Elfo"')
    vida = 25
    defesa = 15
    forca = 35
elif escolhaRaca == 2:
    print('Raça escolhida, "Anão"')
    vida = 30
    defesa = 20
    forca = 40
else:
    print('Escolha inválida!')

# Escolha das habilidades especias da raça escolhida

if escolhaRaca <= 2:
    if escolhaRaca == 0:
        print('''Habilidades disponíveis:
              Nível Extra de Esgrima [0]
              Nível Extra de Adestramento Pets [1]''')
        habilidade_especial = int(input('Escolha: ').strip())
        if habilidade_especial == 0:
            esgrima = 2
            print(f'Nível Extra de Esgrima Aumentado para +{esgrima}')
        elif habilidade_especial == 1:
            adestramento = 2
            print(f'Nível Extra de Adestramento Pets Aumentado para +{adestramento}')
    elif escolhaRaca == 1:
        print('''Habilidades disponíveis:
              Nível Extra de Magia [0]
              Nível Extra de Furtividade [1]''')
        habilidade_especial = int(input('Escolha: ').strip())
        if habilidade_especial == 0:
            magia = 3
            print(f'Nível Extra de Magia Aumentado para +{magia}')
        elif habilidade_especial == 1:
            furtividade = 2
            print(f'Nível Extra de Furtividade Aumentado para +{furtividade}')
    elif escolhaRaca == 2:
        print('''Habilidades disponíveis:
              Nível Extra de Mineração [0]
              Nível Extra de Ferreiro [1]''')
        habilidade_especial = int(input('Escolha: ').strip())
        if habilidade_especial == 0:
            mineracao = 3
            print(f'Nível Extra de Mineração Aumentado para +{mineracao}')
            ferreiro = 2
            print(f'Nível Extra de Ferreiro Aumentado para +{ferreiro}')
sleep(1)
print('Carregando...')
sleep(3.5)
os.system("cls")
sleep(1)

# Execução dos atques

print('Um lobo apareceu!!!')
sleep(1)
print('''Lute com ele, opções de ataque:
      Chute [0]''')
while loboVida > 0:
    ataquePlayer = int(input('Escolha: ').strip())
    if ataquePlayer == 0:
        loboVida = loboVida - forca
        sleep(1)
        vida = vida - loboDano
        if loboVida > 0:
            print(f'Vida lobo "{loboVida}"')
            sleep(0.9)
            print('Lobo atacou!!!')
            sleep(0.9)
        else:
            print(f'Você derrotou o lobo!')
        
        print(f'Você sofreu dano, sua vida agora é {vida}')
    else:
        print('Valor inválido')

