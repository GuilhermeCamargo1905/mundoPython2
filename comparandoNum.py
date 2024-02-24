num = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num > num2:
    print('O primeiro número digitado é maior')
elif num2 > num:
    print('O segundo número digitado é maior')
elif num == num2:
    print('Os dois valores digitados são iguais')