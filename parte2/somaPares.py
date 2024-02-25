soma = 0

for c in range(1,7):
    n1 = int(input('Digite um numero: '))
    if n1 % 2 == 0:
        soma += n1
print('A soma entre os pares é {}'.format(soma))