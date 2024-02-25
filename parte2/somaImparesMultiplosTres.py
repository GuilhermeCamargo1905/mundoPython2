soma = 0
contador = 0
for i in range(0, 501):
    if i % 2 == 1:
        if i % 3 == 0:
            soma += i
            contador += 1

            print(i)

print('A soma de todos os {} valores é {}'.format(contador,soma))

