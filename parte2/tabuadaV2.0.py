num = int(input('dDigite um número que você quer fazer a tabuada: '))

for i in range(0, 11,):
    resultado = num * i
    print('{} X {} = {}'.format(num, i, resultado))