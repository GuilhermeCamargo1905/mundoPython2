from datetime import date

data_nascimento = int(input('Informe a data de nascimento do atleta: '))
idade = date.today().year - data_nascimento

if idade <= 9:
    print('Você está na classificação MIRIM')
elif idade <= 14:
    print('Você é um atleta na classificação NFANTIL')
elif idade <= 19:
    print('Você é um atlteta na classificação JUNIOR')
elif idade <= 20:
    print('Você é um atlteta na classificação SENIOR')
else:
    print('Você é um atleta na classificação MASTER')
