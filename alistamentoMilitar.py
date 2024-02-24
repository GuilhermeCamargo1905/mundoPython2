from datetime import date

ano_Nascimento = int(input('Digite seu ano de nascimento: '))
sexo = str(input('Digite [M] para sexo Masculino\n Digite [F] para sexo Feminino '))

sexo = sexo.upper()

if sexo == 'F':
    print('Você não precisa se alistar')
else:
    ano_Nascimento = int(input('Digite seu ano de nascimento: '))
    ano_atual = date.today().year
    ano_alistamento = ano_Nascimento - ano_atual

    print('Voce tem {} anos SOLDADO'.format(ano_alistamento))

if ano_alistamento < 18:
    print('Você ainda não possui idade para se alistar')

    tempo_passou = 18 - ano_alistamento
    print('Ainda falta {} anos, fique tranquilo SOLDADO!'.format(tempo_passou))

elif ano_alistamento == 18:
    print('Você está na idade de se alistar')

elif ano_alistamento > 18:
    print('Já passou da hora de você se alistar')

    tempo_passou = ano_alistamento - 18
    print('Você deveria ter se alistado a {} anos, vá ao posto de alistamento mais próximo')

