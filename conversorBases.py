num = int(input('Digite um numero: '))

base = int(input('Digite [1] para transformar em binario \n'
                 'Digite [2] para transformar em octal\nDigite [3] para transformar em hexadecimal '))
''
if base == 1:
    conversao = bin(num)[2:]

elif base == 2:
    conversao = oct(num)[2:]

elif base == 3:
    conversao = hex(num)[2:]

else:
    print('Numero invalido')

print('O numero {} convertido para a base {} é {}'.format(num,base,conversao))