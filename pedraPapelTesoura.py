from random import randint
from time import sleep

print('Vamos jogar Jo ken po ? ')

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)


print('''Suas Opções
[0] Pedra 
[1] Pepel 
[2] Tesoura 
''')


jogador = int(input('Escolha a sua opção: '))

print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po')

if computador == 0:
    if jogador == 0:
        print('Temos um empate \nEu escolhi pedra e você também')
    elif jogador == 1:
        print('Você ganhou \nEu escolhi pedra e você escolheu papel')
    elif jogador == 2:
        print('Você Perdeu hehe\nEu escolhi pedra e você escolheu tesoura')
elif computador == 1:
    if jogador == 0:
        print('Você Perdeu hehe\nEu escolhi papel e você escolheu pedra')
    elif jogador == 1:
        print('Temos um empate\nEu escolhi papel e você também')
    elif jogador == 2:
        print('Você ganhou parabens\nEu escolhi papel e você Tesoura')
elif computador == 2:
    if jogador == 0:
        print('Você ganhou parabêns\nEu escolhi Tesoura e você escolheu pedra')
    elif jogador == 1:
        print('Você perdeu hehe\nEu escolhi tesoura e você papel')
    elif jogador == 2:
        print('Temos um empate\n Eu escolhi tesoura e você escolheu tesoura')