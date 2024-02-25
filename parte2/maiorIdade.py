from datetime import date

ano_atual = date.today().year

ano = 0
maiores_idade = 0
menores_idade = 0

for c in range(0,7):
    ano = int(input('Digite o ano do seu nascimento: '))
    idade_pessoa = ano_atual - ano

    if idade_pessoa < 21:
        maiores_idade = maiores_idade + 1
    else:
        menores_idade = menores_idade + 1

print('Maiores de idade: {}'.format(maiores_idade))
print('Menores de idade: {}'.format(menores_idade))
