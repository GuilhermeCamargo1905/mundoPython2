menor = 0
maior = 0

for i in range(1, 6):
    peso = float(input('Digite o peso: '))

    if i == 1:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('Maior peso: {}'.format(maior))
print('Menor peso: {}'.format(menor))