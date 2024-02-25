idade = 0
media = 0
soma = 0
maior = 0
nome_homem_mais_velho = ''
cont_mulheres = 0
for i in range(1, 5):
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite [M] para sexo Masculino\n Digite [F] para sexo Feminino '))
    sexo = sexo.upper()

    soma = soma + idade
    media = soma / i

    if sexo == 'M' and idade > maior:
        maior = idade
        nome_homem_mais_velho = nome

    if sexo == 'F' and idade < maior:
        cont_mulheres +=1

print('A media das idades é de: {:.2f}'.format(media))
print('Nome do homem mais velhp: {}'.format(nome_homem_mais_velho))

if cont_mulheres == 0:
    print('Não temos mulheres no grupo')
else:
    print('Ao todo temos {} mulheres no grupo'.format(cont_mulheres))
